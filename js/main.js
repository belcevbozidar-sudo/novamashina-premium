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

/* ---------- Лизингов калкулатор (продуктова страница) ---------- */
(function () {
  var card = document.querySelector('.calc-card[data-price]');
  if (!card) return;
  var price = parseFloat(card.getAttribute('data-price'));
  var downSel = document.getElementById('ccDown');
  var resSel = document.getElementById('ccResidual');
  var termSel = document.getElementById('ccTerm');
  var RATE = 0.0395;

  function money(eur) {
    return currentCur === 'EUR' ? '€' + fmtNum(eur) + ' с ДДС' : fmtNum(eur * BGN_RATE) + ' лв. с ДДС';
  }
  function recalc() {
    var down = parseFloat(downSel.value) / 100;
    var res = parseFloat(resSel.value) / 100;
    var term = parseInt(termSel.value);
    document.getElementById('ccDownOut').textContent = money(price * down);
    document.getElementById('ccResidualOut').textContent = money(price * res);
    var insOut = document.getElementById('ccInsOut');
    if (insOut) insOut.textContent = money(Math.max(350, price * 0.0107));
    /* анюитетна вноска върху финансираната част с балонна остатъчна стойност */
    var principal = price * (1 - down);
    var r = RATE / 12;
    var balloon = price * res;
    var pay = (principal - balloon / Math.pow(1 + r, term)) * r / (1 - Math.pow(1 + r, -term));
    var big = document.querySelector('.price-box .big .money');
    if (big && pay > 0) {
      big.setAttribute('data-eur', Math.round(pay));
      big.textContent = currentCur === 'EUR' ? '€' + fmtNum(pay) : fmtNum(pay * BGN_RATE) + ' лв.';
    }
  }
  [downSel, resSel, termSel].forEach(function (s) { s.addEventListener('change', recalc); });
  recalc();
})();

/* ---------- Лизингов калкулатор (самостоятелна страница) ---------- */
(function () {
  var priceIn = document.getElementById('lcPrice');
  if (!priceIn) return;
  var downSel = document.getElementById('lcDown');
  var resSel = document.getElementById('lcResidual');
  var termSel = document.getElementById('lcTerm');
  var RATE = 0.0395;
  function recalc() {
    var price = parseFloat(priceIn.value) || 0;
    var down = parseFloat(downSel.value) / 100;
    var res = parseFloat(resSel.value) / 100;
    var term = parseInt(termSel.value);
    document.getElementById('lcPriceBgn').textContent = 'Цена в лв: ' + fmtNum(price * BGN_RATE) + ' лв.';
    document.getElementById('lcDownOut').textContent = '€' + fmtNum(price * down) + ' с ДДС';
    document.getElementById('lcResidualOut').textContent = '€' + fmtNum(price * res) + ' с ДДС';
    var principal = price * (1 - down);
    var r = RATE / 12;
    var balloon = price * res;
    var pay = (principal - balloon / Math.pow(1 + r, term)) * r / (1 - Math.pow(1 + r, -term));
    document.getElementById('lcMonthly').textContent = '€' + fmtNum(Math.max(0, pay));
  }
  [priceIn, downSel, resSel, termSel].forEach(function (s) {
    s.addEventListener('change', recalc);
    s.addEventListener('input', recalc);
  });
  recalc();
})();

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
