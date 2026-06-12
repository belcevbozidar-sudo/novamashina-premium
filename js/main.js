/* NovaMashina.bg — обща клиентска логика */

var BGN_RATE = 1.95583;
var currentCur = 'EUR';

function fmtNum(n) {
  return Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
}

function setCurrency(cur) {
  currentCur = cur;
  document.querySelectorAll('.cur-eur').forEach(function (b) { b.classList.toggle('active', cur === 'EUR'); });
  document.querySelectorAll('.cur-bgn').forEach(function (b) { b.classList.toggle('active', cur === 'BGN'); });
  document.querySelectorAll('.money[data-eur]').forEach(function (el) {
    var eur = parseFloat(el.getAttribute('data-eur'));
    if (isNaN(eur)) return;
    el.textContent = cur === 'EUR' ? '€' + fmtNum(eur) : fmtNum(eur * BGN_RATE) + ' лв.';
  });
}

/* ---------- AI търсачка: анимиран placeholder ---------- */
(function () {
  var input = document.getElementById('aiInput');
  if (!input) return;
  var phrases = [
    'Намери ми икономичен трактор до 150 к.с. за 1 000 €/месец',
    'Търся употребяван комбайн с малко моточасове',
    'Каква сеялка мога да взема с вноска 800 € на месец?',
    'Покажи ми нови трактори с навигация и до 60 м. срок'
  ];
  var pi = 0, ci = 0, deleting = false;
  function tick() {
    var p = phrases[pi];
    if (!deleting) {
      ci++;
      if (ci >= p.length) { deleting = true; setTimeout(tick, 2200); input.placeholder = p; return; }
    } else {
      ci -= 2;
      if (ci <= 0) { ci = 0; deleting = false; pi = (pi + 1) % phrases.length; }
    }
    input.placeholder = p.slice(0, ci) + (deleting ? '' : '|');
    setTimeout(tick, deleting ? 18 : 55);
  }
  tick();
})();

/* ---------- Лизингов калкулатор (Общ двигател за изчисления) ---------- */
var MONTH_NAMES = ['Яну', 'Фев', 'Мар', 'Апр', 'Май', 'Юни', 'Юли', 'Авг', 'Сеп', 'Окт', 'Ноем', 'Дек'];
var startMonthIndex = new Date().getMonth(); // Текущ месец

function calculateLeaseParams(price, pvPct, term, vatType, isNew, selectedMonths) {
  var interestRate = isNew ? 0.035 : 0.045;
  var pv = price * (pvPct / 100);
  var financed = price - pv;
  var fundingFee = financed * 0.01;
  
  var osPercent = 0;
  if (vatType === 'deferred') {
    if (term === 12) osPercent = 20;
    else if (term === 24) osPercent = 15;
    else if (term >= 36) osPercent = 10;
  } else {
    osPercent = 0;
  }
  var os = price * (osPercent / 100);
  
  // Casco: (Цена EUR с ДДС * 0.8%) * 1.02
  var priceWithVat = price * 1.2;
  var casco = (priceWithVat * 0.008) * 1.02;
  
  // Amortization calculation
  var r = interestRate / 12;
  var n = term;
  var pvFactor = 0;
  
  for (var t = 1; t <= n; t++) {
    var calendarMonth = (startMonthIndex + t - 1) % 12;
    var isActive = selectedMonths[calendarMonth] ? 1 : 0;
    if (isActive) {
      if (r > 0) {
        pvFactor += 1 / Math.pow(1 + r, t);
      } else {
        pvFactor += 1;
      }
    }
  }
  
  var pmt = 0;
  if (pvFactor > 0) {
    if (r > 0) {
      pmt = (financed - os / Math.pow(1 + r, n)) / pvFactor;
    } else {
      pmt = (financed - os) / pvFactor;
    }
  }
  
  return {
    pv: pv,
    financed: financed,
    fundingFee: fundingFee,
    osPercent: osPercent,
    os: os,
    casco: casco,
    pmt: pmt,
    interestRate: interestRate
  };
}

function updateMoneyEl(idOrEl, eur) {
  var el = typeof idOrEl === 'string' ? document.getElementById(idOrEl) : idOrEl;
  if (!el) return;
  el.setAttribute('data-eur', Math.round(eur));
  el.textContent = currentCur === 'EUR' ? '€' + fmtNum(eur) : fmtNum(eur * BGN_RATE) + ' лв.';
}

/* ---------- 1. Лизингов калкулатор (Самостоятелна страница) ---------- */
var lcState = 'new';
var lcSelectedMonths = [true, true, true, true, true, true, true, true, true, true, true, true];
var lcScheduleType = 'monthly';
var lcClientType = 'physical';

function initLcCalculator() {
  var priceIn = document.getElementById('lcPrice');
  if (!priceIn) return;
  
  // Render months grid
  var grid = document.getElementById('lcMonthsGrid');
  if (grid) {
    grid.innerHTML = '';
    MONTH_NAMES.forEach(function (mName, idx) {
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'month-btn active disabled';
      btn.textContent = mName;
      btn.setAttribute('data-idx', idx);
      btn.addEventListener('click', function () {
        if (lcScheduleType === 'monthly') return;
        var activeCount = lcSelectedMonths.filter(Boolean).length;
        var currentVal = lcSelectedMonths[idx];
        if (currentVal && activeCount <= 3) {
          alert('Сезонният план изисква избор на минимум 3 месеца за плащане!');
          return;
        }
        lcSelectedMonths[idx] = !currentVal;
        btn.classList.toggle('active', !currentVal);
        recalcLc();
      });
      grid.appendChild(btn);
    });
  }
  
  // Set listeners
  var inputs = ['lcPrice', 'lcDown', 'lcTerm', 'lcVat', 'lcInsPayment'];
  inputs.forEach(function (id) {
    var el = document.getElementById(id);
    if (el) {
      el.addEventListener('change', recalcLc);
      el.addEventListener('input', recalcLc);
    }
  });
  
  recalcLc();
}

function setLcState(state) {
  lcState = state;
  var tabNew = document.getElementById('tabNew');
  var tabUsed = document.getElementById('tabUsed');
  if (tabNew) tabNew.classList.toggle('active', state === 'new');
  if (tabUsed) tabUsed.classList.toggle('active', state === 'used');
  recalcLc();
}

function toggleLcMonths(isSeasonal) {
  lcScheduleType = isSeasonal ? 'seasonal' : 'monthly';
  var grid = document.getElementById('lcMonthsGrid');
  if (!grid) return;
  
  var btns = grid.querySelectorAll('.month-btn');
  if (isSeasonal) {
    // Reset to last 3 active months or keep all
    btns.forEach(function (btn) {
      btn.classList.remove('disabled');
    });
  } else {
    // Reset all to true (monthly)
    lcSelectedMonths = [true, true, true, true, true, true, true, true, true, true, true, true];
    btns.forEach(function (btn) {
      btn.classList.add('active', 'disabled');
    });
  }
  recalcLc();
}

function recalcLc() {
  var priceIn = document.getElementById('lcPrice');
  if (!priceIn) return;
  var price = parseFloat(priceIn.value) || 0;
  var pvPct = parseFloat(document.getElementById('lcDown').value);
  var term = parseInt(document.getElementById('lcTerm').value);
  var vatType = document.getElementById('lcVat').value;
  var isNew = lcState === 'new';
  
  var result = calculateLeaseParams(price, pvPct, term, vatType, isNew, lcSelectedMonths);
  
  // Update UI outputs
  var priceBgnNote = document.getElementById('lcPriceBgn');
  if (priceBgnNote) priceBgnNote.textContent = 'Цена в лв: ' + fmtNum(price * BGN_RATE) + ' лв. без ДДС';
  
  updateMoneyEl('lcDownOut', result.pv);
  updateMoneyEl('lcResidualOut', result.os);
  updateMoneyEl('lcCascoVal', result.casco);
  updateMoneyEl('lcFundingFeeVal', result.fundingFee);
  updateMoneyEl('lcFinalMonthly', result.pmt);
  
  var residualPctEl = document.getElementById('lcResidualPct');
  if (residualPctEl) residualPctEl.value = result.osPercent + '%';
  
  var interestRateEl = document.getElementById('lcInterestRate');
  if (interestRateEl) interestRateEl.value = (result.interestRate * 100).toFixed(1) + '%';
}

function goToLcStep(step) {
  document.querySelectorAll('#lcStep1, #lcStep2, #lcStep3').forEach(function (el) {
    el.classList.remove('active');
  });
  var activeEl = document.getElementById('lcStep' + step);
  if (activeEl) activeEl.classList.add('active');
}

function setLcClientType(type) {
  lcClientType = type;
  var physBtn = document.getElementById('lcClientPhys');
  var legalBtn = document.getElementById('lcClientLegal');
  var physForm = document.getElementById('lcFormPhysical');
  var legalForm = document.getElementById('lcFormLegal');
  
  if (physBtn) physBtn.classList.toggle('active', type === 'physical');
  if (legalBtn) legalBtn.classList.toggle('active', type === 'legal');
  if (physForm) physForm.style.display = type === 'physical' ? 'block' : 'none';
  if (legalForm) legalForm.style.display = type === 'legal' ? 'block' : 'none';
}

function submitLcInquiry() {
  // Simple validation
  var name = lcClientType === 'physical' ? document.getElementById('lcPhysName').value : document.getElementById('lcLegalName').value;
  var phone = lcClientType === 'physical' ? document.getElementById('lcPhysPhone').value : document.getElementById('lcLegalPhone').value;
  if (!name || !phone) {
    alert('Моля попълнете задължителните полета (Име/Фирма и Телефон)!');
    return;
  }
  goToLcStep(3);
}

function resetLcForm() {
  document.getElementById('lcPhysName').value = '';
  document.getElementById('lcPhysEgn').value = '';
  document.getElementById('lcPhysPhone').value = '';
  document.getElementById('lcPhysEmail').value = '';
  document.getElementById('lcPhysAddress').value = '';
  
  document.getElementById('lcLegalName').value = '';
  document.getElementById('lcLegalEik').value = '';
  document.getElementById('lcLegalContact').value = '';
  document.getElementById('lcLegalPhone').value = '';
  document.getElementById('lcLegalEmail').value = '';
  document.getElementById('lcLegalAddress').value = '';
  
  goToLcStep(1);
}

/* ---------- 2. Лизингов калкулатор (Продуктова страница) ---------- */
var ccPrice = 0;
var ccState = 'new';
var ccSelectedMonths = [true, true, true, true, true, true, true, true, true, true, true, true];
var ccScheduleType = 'monthly';
var ccClientType = 'physical';

function initCcCalculator() {
  var card = document.getElementById('prodCalcCard');
  if (!card) return;
  
  ccPrice = parseFloat(card.getAttribute('data-price')) || 0;
  ccState = card.getAttribute('data-state') || 'new';
  
  // Render months grid
  var grid = document.getElementById('ccMonthsGrid');
  if (grid) {
    grid.innerHTML = '';
    MONTH_NAMES.forEach(function (mName, idx) {
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'month-btn active disabled';
      btn.textContent = mName;
      btn.setAttribute('data-idx', idx);
      btn.addEventListener('click', function () {
        if (ccScheduleType === 'monthly') return;
        var activeCount = ccSelectedMonths.filter(Boolean).length;
        var currentVal = ccSelectedMonths[idx];
        if (currentVal && activeCount <= 3) {
          alert('Сезонният план изисква избор на минимум 3 месеца за плащане!');
          return;
        }
        ccSelectedMonths[idx] = !currentVal;
        btn.classList.toggle('active', !currentVal);
        recalcCc();
      });
      grid.appendChild(btn);
    });
  }
  
  // Set listeners
  var inputs = ['ccDown', 'ccTerm', 'ccVat', 'ccInsPayment'];
  inputs.forEach(function (id) {
    var el = document.getElementById(id);
    if (el) {
      el.addEventListener('change', recalcCc);
    }
  });
  
  recalcCc();
}

function toggleCcMonths(isSeasonal) {
  ccScheduleType = isSeasonal ? 'seasonal' : 'monthly';
  var grid = document.getElementById('ccMonthsGrid');
  if (!grid) return;
  
  var btns = grid.querySelectorAll('.month-btn');
  if (isSeasonal) {
    btns.forEach(function (btn) {
      btn.classList.remove('disabled');
    });
  } else {
    ccSelectedMonths = [true, true, true, true, true, true, true, true, true, true, true, true];
    btns.forEach(function (btn) {
      btn.classList.add('active', 'disabled');
    });
  }
  recalcCc();
}

function recalcCc() {
  var card = document.getElementById('prodCalcCard');
  if (!card) return;
  var pvPct = parseFloat(document.getElementById('ccDown').value);
  var term = parseInt(document.getElementById('ccTerm').value);
  var vatType = document.getElementById('ccVat').value;
  var isNew = ccState === 'new';
  
  var result = calculateLeaseParams(ccPrice, pvPct, term, vatType, isNew, ccSelectedMonths);
  
  // Update card outputs
  updateMoneyEl('ccDownOut', result.pv);
  updateMoneyEl('ccResidualOut', result.os);
  updateMoneyEl('ccCascoVal', result.casco);
  updateMoneyEl('ccFundingFeeVal', result.fundingFee);
  
  var residualPctVal = document.getElementById('ccResidualPctVal');
  if (residualPctVal) residualPctVal.textContent = result.osPercent + '%';
  
  var interestRateVal = document.getElementById('ccInterestRateVal');
  if (interestRateVal) interestRateVal.textContent = (result.interestRate * 100).toFixed(1) + '%';
  
  // Update product page main header monthly payment
  var bigMoney = document.querySelector('.price-box .big .money');
  if (bigMoney) {
    updateMoneyEl(bigMoney, result.pmt);
  }
}

function goToCcStep(step) {
  document.querySelectorAll('#pcStep1, #pcStep2, #pcStep3').forEach(function (el) {
    el.classList.remove('active');
  });
  var activeEl = document.getElementById('pcStep' + step);
  if (activeEl) activeEl.classList.add('active');
}

function setCcClientType(type) {
  ccClientType = type;
  var physBtn = document.getElementById('ccClientPhys');
  var legalBtn = document.getElementById('ccClientLegal');
  var physForm = document.getElementById('ccFormPhysical');
  var legalForm = document.getElementById('ccFormLegal');
  
  if (physBtn) physBtn.classList.toggle('active', type === 'physical');
  if (legalBtn) legalBtn.classList.toggle('active', type === 'legal');
  if (physForm) physForm.style.display = type === 'physical' ? 'block' : 'none';
  if (legalForm) legalForm.style.display = type === 'legal' ? 'block' : 'none';
}

function submitCcInquiry() {
  var name = ccClientType === 'physical' ? document.getElementById('ccPhysName').value : document.getElementById('ccLegalName').value;
  var phone = ccClientType === 'physical' ? document.getElementById('ccPhysPhone').value : document.getElementById('ccLegalPhone').value;
  if (!name || !phone) {
    alert('Моля попълнете задължителните полета (Име/Фирма и Телефон)!');
    return;
  }
  goToCcStep(3);
}

function resetCcForm() {
  document.getElementById('ccPhysName').value = '';
  document.getElementById('ccPhysEgn').value = '';
  document.getElementById('ccPhysPhone').value = '';
  document.getElementById('ccPhysEmail').value = '';
  document.getElementById('ccPhysAddress').value = '';
  
  document.getElementById('ccLegalName').value = '';
  document.getElementById('ccLegalEik').value = '';
  document.getElementById('ccLegalContact').value = '';
  document.getElementById('ccLegalPhone').value = '';
  document.getElementById('ccLegalEmail').value = '';
  document.getElementById('ccLegalAddress').value = '';
  
  goToCcStep(1);
}

// Call on window load
window.addEventListener('DOMContentLoaded', function () {
  initLcCalculator();
  initCcCalculator();
  
  // Hamburger menu toggle logic
  var menuToggle = document.getElementById('menuToggle');
  var headerNav = document.querySelector('.header-nav');
  if (menuToggle && headerNav) {
    menuToggle.addEventListener('click', function () {
      menuToggle.classList.toggle('active');
      headerNav.classList.toggle('active');
      document.body.classList.toggle('menu-open');
    });
  }
});

/* ---------- Бюджетен калкулатор ---------- */
(function () {
  var inc = document.getElementById('bfIncome');
  if (!inc) return;
  var loans = document.getElementById('bfLoans');
  var cards = document.getElementById('bfCards');
  function recalc() {
    var income = parseFloat(inc.value) || 0;
    var l = parseFloat(loans.value) || 0;
    var c = (parseFloat(cards.value) || 0) * 0.03; /* 3% от лимита като месечен ангажимент */
    var afford = Math.max(0, income * 0.5 - l - c);
    document.getElementById('bfResult').textContent = '€' + fmtNum(afford);
  }
  [inc, loans, cards].forEach(function (s) { s.addEventListener('input', recalc); });
  recalc();
})();

/* ---------- Галерия (продуктова страница) ---------- */
var galImgs = [];
var galIdx = 0;
(function () {
  var thumbs = document.querySelectorAll('#thumbs .th img');
  if (!thumbs.length) return;
  thumbs.forEach(function (t) { galImgs.push(t.getAttribute('src')); });
})();
function galSet(i) {
  if (!galImgs.length) return;
  galIdx = (i + galImgs.length) % galImgs.length;
  document.getElementById('galMain').src = galImgs[galIdx];
  document.querySelectorAll('#thumbs .th').forEach(function (t, k) {
    t.classList.toggle('active', k === galIdx);
  });
}
function galPrev() { galSet(galIdx - 1); }
function galNext() { galSet(galIdx + 1); }

/* ---------- FAQ е inline (onclick) ---------- */
