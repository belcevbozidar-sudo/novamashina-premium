# Генератор на SVG изображения за novamashina.bg
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def save(name, svg):
    with open(name, 'w') as f:
        f.write(svg.strip())

# ---------- ТРАКТОР (страничен изглед) ----------
def tractor(body, dark, rim='#2b2b2b', cab='#cfe3ef'):
    return f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#dfeef7"/><stop offset="1" stop-color="#f4f8f4"/>
    </linearGradient>
  </defs>
  <rect width="640" height="360" fill="url(#sky)"/>
  <rect y="268" width="640" height="92" fill="#e7e2d6"/>
  <rect y="262" width="640" height="10" fill="#d8d2c2"/>
  <g>
    <rect x="150" y="118" width="210" height="74" rx="14" fill="{body}"/>
    <rect x="150" y="150" width="210" height="42" rx="10" fill="{dark}" opacity=".35"/>
    <rect x="118" y="132" width="52" height="60" rx="10" fill="{body}"/>
    <rect x="126" y="142" width="36" height="26" rx="6" fill="{dark}" opacity=".5"/>
    <rect x="345" y="78" width="118" height="120" rx="14" fill="{dark}"/>
    <rect x="356" y="90" width="96" height="74" rx="10" fill="{cab}"/>
    <rect x="398" y="90" width="8" height="74" fill="{dark}" opacity=".6"/>
    <rect x="345" y="190" width="150" height="34" rx="10" fill="{body}"/>
    <rect x="176" y="96" width="26" height="26" rx="6" fill="{dark}"/>
    <rect x="183" y="58" width="12" height="44" rx="5" fill="#3a3a3a"/>
    <circle cx="216" cy="252" r="52" fill="{rim}"/>
    <circle cx="216" cy="252" r="33" fill="#777"/>
    <circle cx="216" cy="252" r="14" fill="{body}"/>
    <g stroke="#1d1d1d" stroke-width="9">
      <line x1="216" y1="200" x2="216" y2="212"/><line x1="216" y1="292" x2="216" y2="304"/>
      <line x1="164" y1="252" x2="176" y2="252"/><line x1="256" y1="252" x2="268" y2="252"/>
      <line x1="180" y1="216" x2="189" y2="225"/><line x1="243" y1="279" x2="252" y2="288"/>
      <line x1="252" y1="216" x2="243" y2="225"/><line x1="189" y1="279" x2="180" y2="288"/>
    </g>
    <circle cx="442" cy="234" r="74" fill="{rim}"/>
    <circle cx="442" cy="234" r="48" fill="#777"/>
    <circle cx="442" cy="234" r="20" fill="{body}"/>
    <g stroke="#1d1d1d" stroke-width="11">
      <line x1="442" y1="160" x2="442" y2="178"/><line x1="442" y1="290" x2="442" y2="308"/>
      <line x1="368" y1="234" x2="386" y2="234"/><line x1="498" y1="234" x2="516" y2="234"/>
      <line x1="390" y1="182" x2="403" y2="195"/><line x1="481" y1="273" x2="494" y2="286"/>
      <line x1="494" y1="182" x2="481" y2="195"/><line x1="403" y1="273" x2="390" y2="286"/>
    </g>
    <rect x="98" y="186" width="36" height="12" rx="6" fill="#3a3a3a"/>
    <rect x="92" y="192" width="14" height="40" rx="6" fill="#3a3a3a"/>
  </g>
</svg>'''

save('tractor-green.svg',  tractor('#3f9e3f', '#1f6b2d'))
save('tractor-red.svg',    tractor('#c43b2e', '#7d1f16'))
save('tractor-blue.svg',   tractor('#2e6fc4', '#173f7d'))
save('tractor-orange.svg', tractor('#e8762d', '#9e4a14'))
save('tractor-lime.svg',   tractor('#9ec42e', '#5f7d17'))

# ---------- КОМБАЙН ----------
def combine(body, dark):
    return f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360">
  <defs>
    <linearGradient id="sky2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#dfeef7"/><stop offset="1" stop-color="#f4f8f4"/>
    </linearGradient>
  </defs>
  <rect width="640" height="360" fill="url(#sky2)"/>
  <rect y="276" width="640" height="84" fill="#e7e2d6"/>
  <rect y="270" width="640" height="10" fill="#d8d2c2"/>
  <g>
    <rect x="150" y="64" width="240" height="120" rx="16" fill="{body}"/>
    <rect x="150" y="124" width="240" height="60" rx="12" fill="{dark}" opacity=".30"/>
    <rect x="364" y="84" width="92" height="100" rx="12" fill="{dark}"/>
    <rect x="374" y="94" width="72" height="58" rx="8" fill="#cfe3ef"/>
    <rect x="240" y="20" width="16" height="50" fill="#3a3a3a"/>
    <rect x="214" y="14" width="68" height="14" rx="7" fill="#3a3a3a"/>
    <rect x="150" y="184" width="306" height="40" rx="10" fill="{dark}"/>
    <polygon points="120,184 150,150 150,224 120,224" fill="{body}"/>
    <rect x="36" y="210" width="96" height="44" rx="10" fill="#9a9a9a"/>
    <g fill="#6e6e6e">
      <polygon points="40,254 56,210 64,210 48,254"/>
      <polygon points="64,254 80,210 88,210 72,254"/>
      <polygon points="88,254 104,210 112,210 96,254"/>
      <polygon points="112,254 128,210 132,210 120,254"/>
    </g>
    <circle cx="232" cy="268" r="62" fill="#2b2b2b"/>
    <circle cx="232" cy="268" r="40" fill="#777"/>
    <circle cx="232" cy="268" r="17" fill="{body}"/>
    <circle cx="416" cy="284" r="40" fill="#2b2b2b"/>
    <circle cx="416" cy="284" r="25" fill="#777"/>
    <circle cx="416" cy="284" r="11" fill="{body}"/>
    <rect x="456" y="120" width="14" height="120" fill="{dark}"/>
    <rect x="456" y="110" width="60" height="16" rx="8" fill="{dark}"/>
  </g>
</svg>'''

save('combine-yellow.svg', combine('#dfae2c', '#9c7414'))
save('combine-green.svg',  combine('#3f9e3f', '#1f6b2d'))
save('combine-red.svg',    combine('#c43b2e', '#7d1f16'))

# ---------- СЕЯЛКА ----------
save('seeder.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360">
  <defs><linearGradient id="sky3" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#dfeef7"/><stop offset="1" stop-color="#f4f8f4"/></linearGradient></defs>
  <rect width="640" height="360" fill="url(#sky3)"/>
  <rect y="276" width="640" height="84" fill="#e7e2d6"/>
  <rect y="270" width="640" height="10" fill="#d8d2c2"/>
  <rect x="90" y="120" width="460" height="26" rx="10" fill="#3a3a3a"/>
  <g fill="#c43b2e">
    <rect x="110" y="86" width="64" height="56" rx="8"/>
    <rect x="206" y="86" width="64" height="56" rx="8"/>
    <rect x="302" y="86" width="64" height="56" rx="8"/>
    <rect x="398" y="86" width="64" height="56" rx="8"/>
    <rect x="470" y="86" width="64" height="56" rx="8"/>
  </g>
  <g fill="#7d1f16">
    <polygon points="118,142 166,142 150,170 134,170"/>
    <polygon points="214,142 262,142 246,170 230,170"/>
    <polygon points="310,142 358,142 342,170 326,170"/>
    <polygon points="406,142 454,142 438,170 422,170"/>
    <polygon points="478,142 526,142 510,170 494,170"/>
  </g>
  <g stroke="#3a3a3a" stroke-width="8">
    <line x1="142" y1="170" x2="142" y2="252"/><line x1="238" y1="170" x2="238" y2="252"/>
    <line x1="334" y1="170" x2="334" y2="252"/><line x1="430" y1="170" x2="430" y2="252"/>
    <line x1="502" y1="170" x2="502" y2="252"/>
  </g>
  <g fill="#9a9a9a">
    <circle cx="142" cy="262" r="14"/><circle cx="238" cy="262" r="14"/><circle cx="334" cy="262" r="14"/>
    <circle cx="430" cy="262" r="14"/><circle cx="502" cy="262" r="14"/>
  </g>
  <circle cx="200" cy="276" r="34" fill="#2b2b2b"/><circle cx="200" cy="276" r="20" fill="#777"/>
  <circle cx="452" cy="276" r="34" fill="#2b2b2b"/><circle cx="452" cy="276" r="20" fill="#777"/>
  <rect x="40" y="120" width="60" height="14" rx="7" fill="#3a3a3a"/>
  <circle cx="40" cy="127" r="10" fill="#555"/>
</svg>''')

# ---------- ПРЪСКАЧКА ----------
save('sprayer.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360">
  <defs><linearGradient id="sky4" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#dfeef7"/><stop offset="1" stop-color="#f4f8f4"/></linearGradient></defs>
  <rect width="640" height="360" fill="url(#sky4)"/>
  <rect y="276" width="640" height="84" fill="#e7e2d6"/>
  <rect y="270" width="640" height="10" fill="#d8d2c2"/>
  <ellipse cx="320" cy="150" rx="120" ry="64" fill="#2e9e62"/>
  <ellipse cx="320" cy="150" rx="120" ry="64" fill="#footnote" opacity="0"/>
  <ellipse cx="320" cy="136" rx="120" ry="50" fill="#37b873"/>
  <rect x="208" y="150" width="224" height="60" rx="14" fill="#1d6b40"/>
  <g stroke="#3a3a3a" stroke-width="10">
    <line x1="200" y1="180" x2="40" y2="150"/><line x1="440" y1="180" x2="600" y2="150"/>
  </g>
  <g stroke="#1d6b40" stroke-width="6">
    <line x1="60" y1="156" x2="60" y2="186"/><line x1="110" y1="166" x2="110" y2="194"/>
    <line x1="160" y1="174" x2="160" y2="202"/><line x1="480" y1="174" x2="480" y2="202"/>
    <line x1="530" y1="166" x2="530" y2="194"/><line x1="580" y1="156" x2="580" y2="186"/>
  </g>
  <g fill="#7fc8ff" opacity=".75">
    <polygon points="54,190 66,190 72,216 48,216"/><polygon points="104,198 116,198 122,224 98,224"/>
    <polygon points="154,206 166,206 172,232 148,232"/><polygon points="474,206 486,206 492,232 468,232"/>
    <polygon points="524,198 536,198 542,224 518,224"/><polygon points="574,190 586,190 592,216 568,216"/>
  </g>
  <circle cx="252" cy="262" r="46" fill="#2b2b2b"/><circle cx="252" cy="262" r="28" fill="#777"/>
  <circle cx="396" cy="262" r="46" fill="#2b2b2b"/><circle cx="396" cy="262" r="28" fill="#777"/>
  <rect x="150" y="196" width="60" height="14" rx="7" fill="#3a3a3a"/>
</svg>''')

# ---------- РЕМАРКЕ ----------
save('trailer.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360">
  <defs><linearGradient id="sky5" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#dfeef7"/><stop offset="1" stop-color="#f4f8f4"/></linearGradient></defs>
  <rect width="640" height="360" fill="url(#sky5)"/>
  <rect y="276" width="640" height="84" fill="#e7e2d6"/>
  <rect y="270" width="640" height="10" fill="#d8d2c2"/>
  <polygon points="130,110 510,110 478,232 162,232" fill="#c0c8d0"/>
  <polygon points="142,122 498,122 472,220 168,220" fill="#9aa6b2"/>
  <g stroke="#7e8a96" stroke-width="8">
    <line x1="200" y1="116" x2="188" y2="226"/><line x1="280" y1="116" x2="276" y2="226"/>
    <line x1="360" y1="116" x2="364" y2="226"/><line x1="440" y1="116" x2="452" y2="226"/>
  </g>
  <rect x="120" y="98" width="400" height="20" rx="8" fill="#5b6770"/>
  <circle cx="250" cy="276" r="44" fill="#2b2b2b"/><circle cx="250" cy="276" r="26" fill="#777"/>
  <circle cx="390" cy="276" r="44" fill="#2b2b2b"/><circle cx="390" cy="276" r="26" fill="#777"/>
  <g stroke="#3a3a3a" stroke-width="10"><line x1="160" y1="232" x2="60" y2="262"/></g>
  <circle cx="56" cy="264" r="10" fill="#555"/>
  <rect x="486" y="150" width="14" height="82" fill="#5b6770"/>
</svg>''')

# ---------- ИНВЕНТАР (култиватор) ----------
save('cultivator.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360">
  <defs><linearGradient id="sky6" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#dfeef7"/><stop offset="1" stop-color="#f4f8f4"/></linearGradient></defs>
  <rect width="640" height="360" fill="url(#sky6)"/>
  <rect y="276" width="640" height="84" fill="#e7e2d6"/>
  <rect y="270" width="640" height="10" fill="#d8d2c2"/>
  <rect x="110" y="120" width="420" height="22" rx="10" fill="#e8762d"/>
  <rect x="130" y="160" width="380" height="16" rx="8" fill="#e8762d"/>
  <g stroke="#9e4a14" stroke-width="10">
    <line x1="150" y1="142" x2="150" y2="160"/><line x1="320" y1="142" x2="320" y2="160"/><line x1="490" y1="142" x2="490" y2="160"/>
  </g>
  <g stroke="#3a3a3a" stroke-width="9">
    <path d="M150 176 q-6 40 -22 56" fill="none"/><path d="M235 176 q-6 40 -22 56" fill="none"/>
    <path d="M320 176 q-6 40 -22 56" fill="none"/><path d="M405 176 q-6 40 -22 56" fill="none"/>
    <path d="M490 176 q-6 40 -22 56" fill="none"/>
  </g>
  <g fill="#5b6770">
    <polygon points="118,232 138,232 128,258"/><polygon points="203,232 223,232 213,258"/>
    <polygon points="288,232 308,232 298,258"/><polygon points="373,232 393,232 383,258"/>
    <polygon points="458,232 478,232 468,258"/>
  </g>
  <circle cx="200" cy="262" r="30" fill="#2b2b2b"/><circle cx="200" cy="262" r="17" fill="#777"/>
  <circle cx="440" cy="262" r="30" fill="#2b2b2b"/><circle cx="440" cy="262" r="17" fill="#777"/>
  <rect x="48" y="120" width="62" height="14" rx="7" fill="#3a3a3a"/>
  <circle cx="46" cy="127" r="10" fill="#555"/>
</svg>''')

# ---------- HERO ФОН ----------
save('hero-field.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 700" preserveAspectRatio="xMidYMid slice">
  <defs>
    <linearGradient id="hsky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#7db8dd"/><stop offset=".62" stop-color="#cfe6ee"/><stop offset="1" stop-color="#e9f1e2"/>
    </linearGradient>
    <linearGradient id="hfield" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#8fbf4d"/><stop offset="1" stop-color="#5d9636"/>
    </linearGradient>
    <linearGradient id="hfield2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#d9c267"/><stop offset="1" stop-color="#bfa44a"/>
    </linearGradient>
  </defs>
  <rect width="1600" height="700" fill="url(#hsky)"/>
  <circle cx="1290" cy="120" r="70" fill="#fff4c9" opacity=".9"/>
  <ellipse cx="380" cy="140" rx="150" ry="38" fill="#fff" opacity=".75"/>
  <ellipse cx="520" cy="170" rx="110" ry="30" fill="#fff" opacity=".6"/>
  <ellipse cx="1050" cy="100" rx="130" ry="32" fill="#fff" opacity=".65"/>
  <path d="M0 430 Q 400 360 800 420 T 1600 400 V 700 H 0 Z" fill="url(#hfield2)"/>
  <path d="M0 520 Q 500 440 1000 510 T 1600 500 V 700 H 0 Z" fill="url(#hfield)"/>
  <g stroke="#4e7d2d" stroke-width="6" opacity=".5">
    <path d="M120 700 Q 300 580 460 540" fill="none"/>
    <path d="M320 700 Q 480 600 620 555" fill="none"/>
    <path d="M540 700 Q 660 620 780 570" fill="none"/>
    <path d="M760 700 Q 860 630 950 585" fill="none"/>
    <path d="M980 700 Q 1060 640 1130 595" fill="none"/>
    <path d="M1200 700 Q 1260 650 1320 608" fill="none"/>
  </g>
  <g transform="translate(1010,430) scale(1.15)">
    <rect x="60" y="40" width="150" height="56" rx="10" fill="#2f7d33"/>
    <rect x="36" y="50" width="40" height="46" rx="8" fill="#2f7d33"/>
    <rect x="196" y="10" width="78" height="86" rx="10" fill="#1d5422"/>
    <rect x="204" y="20" width="60" height="48" rx="7" fill="#cfe3ef"/>
    <rect x="196" y="92" width="100" height="22" rx="8" fill="#2f7d33"/>
    <circle cx="110" cy="132" r="36" fill="#222"/><circle cx="110" cy="132" r="21" fill="#666"/><circle cx="110" cy="132" r="9" fill="#2f7d33"/>
    <circle cx="252" cy="120" r="52" fill="#222"/><circle cx="252" cy="120" r="32" fill="#666"/><circle cx="252" cy="120" r="13" fill="#2f7d33"/>
    <rect x="84" y="14" width="10" height="32" rx="4" fill="#222"/>
  </g>
  <g fill="#3f6b25" opacity=".85">
    <path d="M60 470 l14 -44 14 44 q-14 10 -28 0z"/><path d="M120 462 l12 -38 12 38 q-12 9 -24 0z"/>
    <path d="M1450 470 l14 -44 14 44 q-14 10 -28 0z"/><path d="M1520 462 l12 -38 12 38 q-12 9 -24 0z"/>
  </g>
</svg>''')

# ---------- КАТЕГОРИЙНИ ИКОНИ (мини машини) ----------
def mini(body, dark, kind):
    if kind == 'tractor':
        inner = f'''<rect x="30" y="64" width="74" height="30" rx="8" fill="{body}"/>
  <rect x="98" y="40" width="44" height="54" rx="8" fill="{dark}"/>
  <rect x="104" y="46" width="32" height="26" rx="5" fill="#cfe3ef"/>
  <circle cx="56" cy="106" r="22" fill="#2b2b2b"/><circle cx="56" cy="106" r="12" fill="#777"/>
  <circle cx="124" cy="98" r="30" fill="#2b2b2b"/><circle cx="124" cy="98" r="18" fill="#777"/>
  <rect x="40" y="48" width="10" height="18" fill="#333"/>'''
    elif kind == 'combine':
        inner = f'''<rect x="34" y="38" width="76" height="44" rx="9" fill="{body}"/>
  <rect x="104" y="46" width="34" height="38" rx="7" fill="{dark}"/>
  <rect x="110" y="52" width="22" height="20" rx="4" fill="#cfe3ef"/>
  <rect x="34" y="78" width="104" height="16" rx="7" fill="{dark}"/>
  <rect x="8" y="86" width="30" height="18" rx="6" fill="#9a9a9a"/>
  <circle cx="64" cy="106" r="20" fill="#2b2b2b"/><circle cx="64" cy="106" r="11" fill="#777"/>
  <circle cx="120" cy="108" r="14" fill="#2b2b2b"/><circle cx="120" cy="108" r="8" fill="#777"/>'''
    elif kind == 'seeder':
        inner = f'''<rect x="16" y="52" width="140" height="10" rx="5" fill="#3a3a3a"/>
  <rect x="26" y="36" width="26" height="22" rx="4" fill="{body}"/><rect x="62" y="36" width="26" height="22" rx="4" fill="{body}"/>
  <rect x="98" y="36" width="26" height="22" rx="4" fill="{body}"/><rect x="128" y="36" width="26" height="22" rx="4" fill="{body}"/>
  <g stroke="#3a3a3a" stroke-width="5"><line x1="39" y1="62" x2="39" y2="98"/><line x1="75" y1="62" x2="75" y2="98"/><line x1="111" y1="62" x2="111" y2="98"/><line x1="141" y1="62" x2="141" y2="98"/></g>
  <circle cx="39" cy="104" r="8" fill="#777"/><circle cx="75" cy="104" r="8" fill="#777"/><circle cx="111" cy="104" r="8" fill="#777"/><circle cx="141" cy="104" r="8" fill="#777"/>'''
    elif kind == 'sprayer':
        inner = f'''<ellipse cx="86" cy="58" rx="38" ry="24" fill="{body}"/>
  <rect x="52" y="62" width="68" height="22" rx="8" fill="{dark}"/>
  <g stroke="#3a3a3a" stroke-width="6"><line x1="52" y1="72" x2="6" y2="62"/><line x1="120" y1="72" x2="166" y2="62"/></g>
  <g stroke="{dark}" stroke-width="4"><line x1="20" y1="66" x2="20" y2="82"/><line x1="148" y1="66" x2="148" y2="82"/></g>
  <circle cx="66" cy="98" r="16" fill="#2b2b2b"/><circle cx="66" cy="98" r="9" fill="#777"/>
  <circle cx="108" cy="98" r="16" fill="#2b2b2b"/><circle cx="108" cy="98" r="9" fill="#777"/>'''
    elif kind == 'trailer':
        inner = f'''<polygon points="28,44 148,44 138,86 38,86" fill="#c0c8d0"/>
  <rect x="24" y="38" width="128" height="9" rx="4" fill="#5b6770"/>
  <g stroke="#7e8a96" stroke-width="4"><line x1="60" y1="46" x2="56" y2="84"/><line x1="92" y1="46" x2="92" y2="84"/><line x1="124" y1="46" x2="128" y2="84"/></g>
  <circle cx="66" cy="100" r="15" fill="#2b2b2b"/><circle cx="66" cy="100" r="8" fill="#777"/>
  <circle cx="112" cy="100" r="15" fill="#2b2b2b"/><circle cx="112" cy="100" r="8" fill="#777"/>
  <g stroke="#3a3a3a" stroke-width="5"><line x1="38" y1="86" x2="10" y2="96"/></g>'''
    else:  # inventar
        inner = f'''<rect x="20" y="46" width="132" height="10" rx="5" fill="{body}"/>
  <rect x="28" y="64" width="116" height="8" rx="4" fill="{body}"/>
  <g stroke="#3a3a3a" stroke-width="5">
    <path d="M44 72 q-3 18 -11 26" fill="none"/><path d="M86 72 q-3 18 -11 26" fill="none"/><path d="M128 72 q-3 18 -11 26" fill="none"/>
  </g>
  <g fill="#5b6770"><polygon points="26,98 40,98 33,112"/><polygon points="68,98 82,98 75,112"/><polygon points="110,98 124,98 117,112"/></g>'''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 172 124">{inner}</svg>'

save('cat-tractors.svg',   mini('#3f9e3f', '#1f6b2d', 'tractor'))
save('cat-combines.svg',   mini('#dfae2c', '#9c7414', 'combine'))
save('cat-seeders.svg',    mini('#c43b2e', '#7d1f16', 'seeder'))
save('cat-sprayers.svg',   mini('#37b873', '#1d6b40', 'sprayer'))
save('cat-trailers.svg',   mini('#9aa6b2', '#5b6770', 'trailer'))
save('cat-inventar.svg',   mini('#e8762d', '#9e4a14', 'inventar'))

# ---------- НОВИНИ изображения ----------
def news_img(c1, c2, motif):
    return f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 680" preserveAspectRatio="xMidYMid slice">
  <defs><linearGradient id="ng" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs>
  <rect width="600" height="680" fill="url(#ng)"/>
  {motif}
</svg>'''

wheat = '<g stroke="#fff" stroke-width="7" opacity=".55" fill="none">' + ''.join(
    f'<path d="M{80+i*90} 560 q-8 -90 12 -170"/><circle cx="{92+i*90}" cy="380" r="16"/>' for i in range(6)) + '</g>'
save('news-1.svg', news_img('#5d9636', '#2f5d1c', wheat))
gears = '<g fill="#fff" opacity=".4"><circle cx="180" cy="240" r="70"/><circle cx="180" cy="240" r="36" fill="#3b6f23"/><circle cx="360" cy="420" r="100"/><circle cx="360" cy="420" r="52" fill="#3b6f23"/></g>'
save('news-2.svg', news_img('#4d8a2c', '#1f4a14', gears))
road = '<path d="M260 680 L300 200 L340 680 Z" fill="#fff" opacity=".35"/><circle cx="300" cy="150" r="60" fill="#fff4c9" opacity=".8"/>'
save('news-3.svg', news_img('#7db8dd', '#33647e', road))
chart = '<g fill="#fff" opacity=".5"><rect x="120" y="420" width="60" height="140"/><rect x="220" y="350" width="60" height="210"/><rect x="320" y="280" width="60" height="280"/><rect x="420" y="200" width="60" height="360"/></g><path d="M120 380 L240 300 L350 240 L470 150" stroke="#fff" stroke-width="10" fill="none"/>'
save('news-4.svg', news_img('#3f9e3f', '#0e4d2c', chart))
drop = '<g fill="#fff" opacity=".45"><path d="M300 160 q90 130 0 200 q-90 -70 0 -200z"/><circle cx="180" cy="480" r="50"/><circle cx="420" cy="480" r="50"/></g>'
save('news-5.svg', news_img('#37b873', '#14532d', drop))
snow = '<g stroke="#fff" stroke-width="8" opacity=".55"><line x1="150" y1="180" x2="150" y2="280"/><line x1="100" y1="230" x2="200" y2="230"/><line x1="115" y1="195" x2="185" y2="265"/><line x1="185" y1="195" x2="115" y2="265"/><line x1="430" y1="380" x2="430" y2="500"/><line x1="370" y1="440" x2="490" y2="440"/><line x1="388" y1="398" x2="472" y2="482"/><line x1="472" y1="398" x2="388" y2="482"/></g>'
save('news-6.svg', news_img('#6aa6c8', '#2c5570', snow))

# ---------- ABOUT илюстрации ----------
save('about-1.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 420">
  <ellipse cx="260" cy="225" rx="240" ry="180" fill="#eef7ee"/>
  <rect x="150" y="80" width="220" height="280" rx="22" fill="#2c3e50"/>
  <rect x="166" y="100" width="188" height="240" rx="12" fill="#fff"/>
  <rect x="186" y="124" width="64" height="44" rx="8" fill="#e6e6e6"/>
  <rect x="186" y="180" width="148" height="10" rx="5" fill="#e0e0e0"/>
  <rect x="186" y="200" width="110" height="10" rx="5" fill="#e0e0e0"/>
  <rect x="186" y="236" width="64" height="44" rx="8" fill="#caebca"/>
  <g transform="translate(196,244) scale(.30)"><rect x="10" y="30" width="80" height="32" rx="8" fill="#3f9e3f"/><rect x="78" y="10" width="40" height="52" rx="8" fill="#1f6b2d"/><circle cx="36" cy="74" r="18" fill="#2b2b2b"/><circle cx="98" cy="70" r="24" fill="#2b2b2b"/></g>
  <rect x="186" y="292" width="148" height="10" rx="5" fill="#e0e0e0"/>
  <path d="M330 320 q60 30 60 90 l-50 10 q-30 -50 -10 -100z" fill="#f0b27a"/>
  <path d="M300 270 l70 64 -28 30 -70 -64z" fill="#f0b27a"/>
  <path d="M260 330 q40 -20 70 6 l-18 60 q-50 10 -70 -20z" fill="#4dbc4d"/>
</svg>''')

save('about-2.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 420">
  <ellipse cx="260" cy="230" rx="240" ry="175" fill="#eef7ee"/>
  <rect x="120" y="120" width="130" height="90" rx="10" fill="#fff" stroke="#e0e0e0" stroke-width="3"/>
  <g transform="translate(134,138) scale(.42)"><rect x="10" y="30" width="80" height="32" rx="8" fill="#3f9e3f"/><rect x="78" y="10" width="40" height="52" rx="8" fill="#1f6b2d"/><circle cx="36" cy="74" r="18" fill="#2b2b2b"/><circle cx="98" cy="70" r="24" fill="#2b2b2b"/></g>
  <path d="M150 196 l16 12 26 -30" stroke="#4dbc4d" stroke-width="7" fill="none" stroke-linecap="round"/>
  <rect x="280" y="150" width="110" height="130" rx="10" fill="#fff" stroke="#e0e0e0" stroke-width="3"/>
  <text x="304" y="208" font-family="Arial" font-size="44" fill="#cfcfcf">$</text>
  <text x="338" y="238" font-family="Arial" font-size="34" fill="#4dbc4d">%</text>
  <path d="M306 252 l12 10 22 -26" stroke="#4dbc4d" stroke-width="6" fill="none" stroke-linecap="round"/>
  <circle cx="200" cy="300" r="42" fill="#f6c34f"/>
  <path d="M170 330 q30 30 80 12 l-6 50 q-50 14 -86 -16z" fill="#2c3e50"/>
  <circle cx="208" cy="282" r="22" fill="#f0b27a"/>
  <path d="M236 300 l60 -16 6 22 -58 18z" fill="#f0b27a"/>
  <path d="M120 360 q90 36 180 8" stroke="#caebca" stroke-width="14" fill="none" stroke-linecap="round"/>
</svg>''')

# ---------- БЮДЖЕТЕН КАЛКУЛАТОР герой ----------
save('budget-hero.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 460">
  <ellipse cx="380" cy="240" rx="330" ry="180" fill="#eef7ee"/>
  <rect x="120" y="220" width="180" height="120" rx="18" fill="#b98d4f"/>
  <rect x="138" y="240" width="144" height="80" rx="10" fill="#a3793e" stroke="#8a6531" stroke-width="4" stroke-dasharray="10 8"/>
  <circle cx="282" cy="280" r="16" fill="#6e5126"/>
  <circle cx="560" cy="320" r="58" fill="#f6c34f"/>
  <text x="540" y="340" font-family="Arial" font-size="52" fill="#b98d18">€</text>
  <g transform="translate(430,120)">
    <circle cx="40" cy="20" r="26" fill="#f0b27a"/>
    <path d="M14 44 q26 -18 52 0 l-6 70 h-40z" fill="#4dbc4d"/>
    <path d="M60 70 q30 6 44 -18" stroke="#f0b27a" stroke-width="14" fill="none" stroke-linecap="round"/>
    <rect x="96" y="20" width="26" height="40" rx="6" fill="#f6c34f"/>
    <path d="M30 112 q-10 60 16 96 l22 -6 q-14 -40 0 -88z" fill="#2c3e50"/>
  </g>
  <g transform="translate(560,90) scale(.8)"><path d="M40 60 q0 -36 36 -36 q10 -18 32 -12 q20 -16 40 0 q30 -6 34 24 q20 10 8 34z" fill="#fff"/></g>
  <g transform="translate(120,110)"><circle cx="30" cy="24" r="18" fill="#f0b27a"/><path d="M12 40 q18 -12 36 0 l-4 48 h-28z" fill="#c43b2e"/><circle cx="74" cy="38" r="12" fill="#f0b27a"/><path d="M62 48 q12 -8 24 0 l-3 34 h-18z" fill="#2e6fc4"/></g>
  <rect x="540" y="200" width="120" height="80" rx="12" fill="#7db8dd" opacity=".85"/>
  <path d="M556 264 l22 -26 18 14 26 -34" stroke="#fff" stroke-width="8" fill="none" stroke-linecap="round"/>
</svg>''')

save('budget-side.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 460">
  <ellipse cx="280" cy="240" rx="260" ry="180" fill="#eef7ee"/>
  <rect x="90" y="150" width="240" height="160" rx="14" fill="#fff" stroke="#e0e0e0" stroke-width="4"/>
  <rect x="110" y="174" width="90" height="10" rx="5" fill="#e0e0e0"/>
  <rect x="110" y="196" width="200" height="10" rx="5" fill="#e6e6e6"/>
  <g fill="#4dbc4d"><rect x="116" y="250" width="26" height="44"/><rect x="156" y="226" width="26" height="68"/><rect x="196" y="206" width="26" height="88"/><rect x="236" y="240" width="26" height="54" fill="#f6c34f"/><rect x="276" y="216" width="26" height="78" fill="#e8762d"/></g>
  <path d="M250 120 L320 60 L390 130 q-34 60 -140 60z" fill="#4dbc4d" opacity="0"/>
  <path d="M150 120 q90 -60 180 -10" stroke="#4dbc4d" stroke-width="12" fill="none" stroke-linecap="round"/>
  <polygon points="338,98 346,128 314,122" fill="#4dbc4d"/>
  <g transform="translate(340,200)">
    <circle cx="46" cy="26" r="26" fill="#f0b27a"/>
    <path d="M20 50 q26 -16 52 0 l-8 84 h-38z" fill="#2f7d33"/>
    <path d="M30 132 q-8 50 12 80 l20 -4 q-10 -36 2 -76z" fill="#2c3e50"/>
    <rect x="80" y="60" width="70" height="50" rx="8" fill="#f6c34f"/>
    <circle cx="115" cy="85" r="12" fill="#b98d18"/>
  </g>
  <g fill="#f6c34f"><circle cx="130" cy="370" r="22"/><circle cx="172" cy="382" r="22"/><circle cx="214" cy="370" r="22"/></g>
  <text x="120" y="378" font-family="Arial" font-size="22" fill="#a07908">€</text>
  <text x="162" y="390" font-family="Arial" font-size="22" fill="#a07908">€</text>
  <text x="204" y="378" font-family="Arial" font-size="22" fill="#a07908">€</text>
</svg>''')

# ---------- КАРТА за контакти ----------
save('map.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 800" preserveAspectRatio="xMidYMid slice">
  <rect width="1600" height="800" fill="#e8ecde"/>
  <g stroke="#ffffff" stroke-width="22" fill="none" opacity=".9">
    <path d="M-20 200 H 1620"/><path d="M-20 480 H 1620"/>
    <path d="M300 -20 V 820"/><path d="M760 -20 V 820"/><path d="M1180 -20 V 820"/>
  </g>
  <g stroke="#fff" stroke-width="10" fill="none" opacity=".8">
    <path d="M-20 340 q400 60 760 0 t880 30"/><path d="M520 -20 q40 400 -60 840"/><path d="M980 -20 q-30 380 60 840"/>
  </g>
  <g fill="#d4e6c3">
    <rect x="60" y="60" width="180" height="100" rx="10"/><rect x="1280" y="560" width="220" height="140" rx="10"/>
    <rect x="840" y="80" width="240" height="80" rx="10"/><rect x="360" y="560" width="280" height="160" rx="10"/>
  </g>
  <g fill="#cfd6db">
    <rect x="340" y="240" width="160" height="90" rx="6"/><rect x="800" y="520" width="120" height="90" rx="6"/>
    <rect x="1220" y="240" width="200" height="80" rx="6"/><rect x="80" y="520" width="140" height="110" rx="6"/>
  </g>
  <g transform="translate(770,330)">
    <path d="M30 0 C 12 0 0 14 0 32 c0 24 30 56 30 56 s30 -32 30 -56 C 60 14 48 0 30 0z" fill="#c0392b"/>
    <circle cx="30" cy="30" r="12" fill="#fff"/>
  </g>
</svg>''')

# ---------- ПРОМО банери ----------
save('promo-fleet.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 400" preserveAspectRatio="xMidYMid slice">
  <defs><linearGradient id="pf" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#a8c8e0"/><stop offset=".6" stop-color="#d8e4d2"/><stop offset="1" stop-color="#c2b98a"/></linearGradient></defs>
  <rect width="640" height="400" fill="url(#pf)"/>
  <rect y="300" width="640" height="100" fill="#b3a76e"/>
  <g transform="translate(40,180) scale(.55)"><rect x="60" y="40" width="150" height="56" rx="10" fill="#c43b2e"/><rect x="196" y="10" width="78" height="86" rx="10" fill="#7d1f16"/><rect x="204" y="20" width="60" height="48" rx="7" fill="#cfe3ef"/><circle cx="110" cy="132" r="36" fill="#222"/><circle cx="252" cy="120" r="52" fill="#222"/><circle cx="252" cy="120" r="30" fill="#666"/><circle cx="110" cy="132" r="20" fill="#666"/></g>
  <g transform="translate(230,160) scale(.62)"><rect x="60" y="40" width="150" height="56" rx="10" fill="#2e6fc4"/><rect x="196" y="10" width="78" height="86" rx="10" fill="#173f7d"/><rect x="204" y="20" width="60" height="48" rx="7" fill="#cfe3ef"/><circle cx="110" cy="132" r="36" fill="#222"/><circle cx="252" cy="120" r="52" fill="#222"/><circle cx="252" cy="120" r="30" fill="#666"/><circle cx="110" cy="132" r="20" fill="#666"/></g>
  <g transform="translate(430,140) scale(.7)"><rect x="60" y="40" width="150" height="56" rx="10" fill="#3f9e3f"/><rect x="196" y="10" width="78" height="86" rx="10" fill="#1f6b2d"/><rect x="204" y="20" width="60" height="48" rx="7" fill="#cfe3ef"/><circle cx="110" cy="132" r="36" fill="#222"/><circle cx="252" cy="120" r="52" fill="#222"/><circle cx="252" cy="120" r="30" fill="#666"/><circle cx="110" cy="132" r="20" fill="#666"/></g>
</svg>''')

save('promo-harvest.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 400" preserveAspectRatio="xMidYMid slice">
  <defs><linearGradient id="ph" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#f2d98c"/><stop offset="1" stop-color="#caa64e"/></linearGradient></defs>
  <rect width="640" height="400" fill="url(#ph)"/>
  <circle cx="540" cy="80" r="54" fill="#fff4c9"/>
  <rect y="310" width="640" height="90" fill="#b3924a"/>
  <g stroke="#9c7c38" stroke-width="6" opacity=".7">
    <line x1="30" y1="400" x2="80" y2="310"/><line x1="120" y1="400" x2="170" y2="310"/><line x1="210" y1="400" x2="260" y2="310"/>
    <line x1="300" y1="400" x2="350" y2="310"/><line x1="390" y1="400" x2="440" y2="310"/><line x1="480" y1="400" x2="530" y2="310"/>
  </g>
  <g transform="translate(150,120) scale(.85)">
    <rect x="34" y="38" width="180" height="80" rx="12" fill="#dfae2c"/>
    <rect x="200" y="50" width="70" height="70" rx="10" fill="#9c7414"/>
    <rect x="210" y="60" width="50" height="36" rx="6" fill="#cfe3ef"/>
    <rect x="34" y="112" width="240" height="26" rx="9" fill="#9c7414"/>
    <rect x="-30" y="124" width="68" height="30" rx="8" fill="#9a9a9a"/>
    <circle cx="96" cy="158" r="38" fill="#2b2b2b"/><circle cx="96" cy="158" r="22" fill="#777"/>
    <circle cx="226" cy="166" r="26" fill="#2b2b2b"/><circle cx="226" cy="166" r="15" fill="#777"/>
  </g>
</svg>''')

print("OK:", len([f for f in os.listdir('.') if f.endswith('.svg')]), "svg files")
