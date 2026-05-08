
const GEO = 'https://geocoding-api.open-meteo.com/v1/search';
const WX  = 'https://api.open-meteo.com/v1/forecast';
const IMG = 'https://openweathermap.org/img/wn/';

let unit = 'celsius';  // celsius | fahrenheit //
let cityName = 'New Delhi';
let weekMode = false;
let showingAll = false;

const el = {
  city:      document.getElementById('cityName'),
  day:       document.getElementById('dayName'),
  date:      document.getElementById('dateStr'),
  temp:      document.getElementById('mainTemp'),
  hilo:      document.getElementById('hiLo'),
  img:       document.getElementById('mainWeatherImg'),
  cond:      document.getElementById('condition'),
  feels:     document.getElementById('feelsLike'),
  hum:       document.getElementById('humidity'),
  wind:      document.getElementById('wind'),
  vis:       document.getElementById('visibility'),
  sunrise:   document.getElementById('sunrise'),
  sunset:    document.getElementById('sunset'),
  daylen:    document.getElementById('dayLength'),
  tomTemp:   document.getElementById('tomorrowTemp'),
  tomIcon:   document.getElementById('tomorrowIcon'),
  hourly:    document.getElementById('hourlyRow'),
  rainPct:   document.getElementById('rainChance'),
  rainBar:   document.getElementById('rainBar'),
  uvNum:     document.getElementById('uvVal'),
  uvArc:     document.getElementById('uvArc'),
  uvLabel:   document.getElementById('uvText'),
  windNum:   document.getElementById('windSpeed'),
  windDir:   document.getElementById('windDirText'),
  humNum:    document.getElementById('humVal'),
  humBar:    document.getElementById('humBar'),
  cities:    document.getElementById('citiesGrid'),
  loader:    document.getElementById('loaderOverlay'),
  toast:     document.getElementById('toast'),
  search:    document.getElementById('searchInput'),
  searchBtn: document.getElementById('searchBtn'),
  cBtn:      document.getElementById('celsiusBtn'),
  fBtn:      document.getElementById('fahrenheitBtn'),
  tabDay:    document.getElementById('tab-today'),
  tabWeek:   document.getElementById('tab-week'),
  seeAll:    document.getElementById('seeAllBtn'),
};

const defaultCities = ['Mumbai', 'Dubai', 'London', 'Tokyo'];
const allCities = [...defaultCities, 'New York', 'Sydney', 'Paris', 'Singapore'];

// helpers //
const showLoader = () => el.loader.classList.add('visible');
const hideLoader = () => el.loader.classList.remove('visible');
const sym = () => unit === 'celsius' ? '°C' : '°F';
const fmtTemp = v => Math.round(v) + sym();

function toast(msg, type = '') {
  el.toast.textContent = msg;
  el.toast.className = 'toast show ' + type;
  setTimeout(() => el.toast.className = 'toast', 3500);
}

const DAYS = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
const MONTHS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];

function getDayName(dateStr) {
  return DAYS[new Date(dateStr).getDay()];
}

function fmtDate(dateStr) {
  const d = new Date(dateStr);
  return `${d.getDate()} ${MONTHS[d.getMonth()]}, ${d.getFullYear()}`;
}

function fmtTime(isoStr) {
  const d = new Date(isoStr);
  let h = d.getHours(), m = d.getMinutes();
  const ap = h >= 12 ? 'PM' : 'AM';
  h = h % 12 || 12;
  return `${h}:${String(m).padStart(2,'0')} ${ap}`;
}

function dayLength(rise, set) {
  const diff = (new Date(set) - new Date(rise)) / 1000;
  return `${Math.floor(diff / 3600)}h ${Math.floor((diff % 3600) / 60)}m`;
}

function degToDir(deg) {
  return ['N','NE','E','SE','S','SW','W','NW'][Math.round(deg / 45) % 8];
}

//  weather code → label + icon //
function wmoInfo(code) {
  const map = {
    0:  { label: 'Clear Sky',       icon: '01d' },
    1:  { label: 'Mainly Clear',    icon: '01d' },
    2:  { label: 'Partly Cloudy',   icon: '02d' },
    3:  { label: 'Overcast',        icon: '04d' },
    45: { label: 'Foggy',           icon: '50d' },
    48: { label: 'Icy Fog',         icon: '50d' },
    51: { label: 'Light Drizzle',   icon: '09d' },
    53: { label: 'Drizzle',         icon: '09d' },
    55: { label: 'Heavy Drizzle',   icon: '09d' },
    61: { label: 'Light Rain',      icon: '10d' },
    63: { label: 'Rain',            icon: '10d' },
    65: { label: 'Heavy Rain',      icon: '10d' },
    71: { label: 'Light Snow',      icon: '13d' },
    73: { label: 'Snow',            icon: '13d' },
    75: { label: 'Heavy Snow',      icon: '13d' },
    80: { label: 'Rain Showers',    icon: '09d' },
    81: { label: 'Showers',         icon: '09d' },
    82: { label: 'Heavy Showers',   icon: '09d' },
    95: { label: 'Thunderstorm',    icon: '11d' },
    99: { label: 'Hail Storm',      icon: '11d' },
  };
  return map[code] || { label: 'Clear', icon: '01d' };
}

function setUV(val) {
  const v = Math.round(val);
  el.uvNum.textContent = v;
  el.uvArc.style.strokeDashoffset = 201 - (201 * Math.min(v, 11) / 11);
  const levels = ['Low','Moderate','High','Very High','Extreme'];
  const colors = ['#34d399','#f5a623','#f87171','#ef4444','#b91c1c'];
  const i = v <= 2 ? 0 : v <= 5 ? 1 : v <= 7 ? 2 : v <= 10 ? 3 : 4;
  el.uvLabel.textContent = levels[i];
  el.uvArc.style.stroke = colors[i];
}

// geocode city name → { lat, lon, name, timezone } //
async function geocode(q) {
  const res = await fetch(`${GEO}?name=${encodeURIComponent(q)}&count=1&language=en&format=json`);
  const d = await res.json();
  if (!d.results || d.results.length === 0) throw new Error(`City "${q}" not found`);
  const r = d.results[0];
  return { lat: r.latitude, lon: r.longitude, name: r.name, country: r.country_code, timezone: r.timezone };
}

// fetch weather from Open-Meteo //
async function getWeather(lat, lon, timezone) {
  const params = [
    `latitude=${lat}`,
    `longitude=${lon}`,
    `timezone=${encodeURIComponent(timezone)}`,
    `current=temperature_2m,apparent_temperature,relative_humidity_2m,wind_speed_10m,wind_direction_10m,weather_code,visibility`,
    `hourly=temperature_2m,weather_code,precipitation_probability`,
    `daily=weather_code,temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max,precipitation_probability_max`,
    `wind_speed_unit=kmh`,
    unit === 'fahrenheit' ? 'temperature_unit=fahrenheit' : '',
    `forecast_days=7`,
  ].filter(Boolean).join('&');

  const res = await fetch(`${WX}?${params}`);
  return res.json();
}

// main fetch + render //
async function fetchCity(q) {
  showLoader();
  try {
    const geo = await geocode(q);
    const wx  = await getWeather(geo.lat, geo.lon, geo.timezone);
    renderAll(geo, wx);
    cityName = q;
    toast(`Updated: ${geo.name}`, 'success');
  } catch (err) {
    toast(err.message || 'Something went wrong', 'error');
  } finally {
    hideLoader();
  }
}

function renderAll(geo, wx) {
  const c = wx.current;
  const d = wx.daily;
  const h = wx.hourly;
  const info = wmoInfo(c.weather_code);
  const today = new Date().toISOString().slice(0, 10);

  // main card //
  el.city.textContent  = geo.name;
  el.day.textContent   = getDayName(today);
  el.date.textContent  = fmtDate(today);
  el.temp.textContent  = fmtTemp(c.temperature_2m);
  el.hilo.textContent  = `High: ${fmtTemp(d.temperature_2m_max[0])}  Low: ${fmtTemp(d.temperature_2m_min[0])}`;
  el.cond.textContent  = info.label;
  el.feels.textContent = `Feels Like: ${fmtTemp(c.apparent_temperature)}`;
  el.hum.textContent   = `${c.relative_humidity_2m}%`;
  el.wind.textContent  = `${Math.round(c.wind_speed_10m)} km/h`;
  el.vis.textContent   = c.visibility ? `${(c.visibility / 1000).toFixed(1)} km` : 'N/A';
  el.img.src           = `${IMG}${info.icon}@2x.png`;
  el.img.alt           = info.label;

  // sun //
  el.sunrise.textContent = fmtTime(d.sunrise[0]);
  el.sunset.textContent  = fmtTime(d.sunset[0]);
  el.daylen.textContent  = dayLength(d.sunrise[0], d.sunset[0]);

  // tomorrow //
  el.tomTemp.textContent = fmtTemp(d.temperature_2m_max[1]);
  const tomInfo = wmoInfo(d.weather_code[1]);
  el.tomIcon.innerHTML = `<img src="${IMG}${tomInfo.icon}@2x.png" width="28" height="28" alt="" />`;

  // highlights //
  el.humNum.textContent  = `${c.relative_humidity_2m}%`;
  el.windNum.textContent = Math.round(c.wind_speed_10m);
  el.windDir.textContent = degToDir(c.wind_direction_10m);
  setUV(d.uv_index_max[0] || 0);

  const rain = d.precipitation_probability_max[0] || 0;
  el.rainPct.textContent = `${rain}%`;
  setTimeout(() => {
    el.humBar.style.width  = `${c.relative_humidity_2m}%`;
    el.rainBar.style.width = `${rain}%`;
  }, 100);

  // hourly or weekly // 
  weekMode ? renderWeekly(d) : renderHourly(h);
}

function makeHourCard(label, iconCode, temp, active) {
  const div = document.createElement('div');
  div.className = 'hourly-item' + (active ? ' active-hour' : '');
  div.innerHTML = `
    <span class="hour-label">${label}</span>
    <img src="${IMG}${wmoInfo(iconCode).icon}@2x.png" width="30" height="30" alt="" />
    <span class="hour-temp">${typeof temp === 'number' ? fmtTemp(temp) : temp}</span>
  `;
  div.addEventListener('click', () => {
    document.querySelectorAll('.hourly-item').forEach(x => x.classList.remove('active-hour'));
    div.classList.add('active-hour');
  });
  return div;
}

function renderHourly(h) {
  el.hourly.innerHTML = '';
  // get next 8 hours from current hour //
  const now = new Date().getHours();
  const times = h.time;
  let count = 0;
  for (let i = 0; i < times.length && count < 8; i++) {
    const hr = new Date(times[i]).getHours();
    const d  = new Date(times[i]);
    // only show from current time onward on today
    if (d < new Date() - 3600000) continue;
    const label = `${hr % 12 || 12}${hr >= 12 ? 'PM' : 'AM'}`;
    el.hourly.appendChild(makeHourCard(label, h.weather_code[i], h.temperature_2m[i], count === 0));
    count++;
  }
}

function renderWeekly(d) {
  el.hourly.innerHTML = '';
  d.time.slice(0, 7).forEach((t, i) => {
    const label = i === 0 ? 'Today' : DAYS[new Date(t).getDay()].slice(0, 3);
    el.hourly.appendChild(makeHourCard(label, d.weather_code[i], d.temperature_2m_max[i], i === 0));
  });
}

// load other cities //
async function loadCities(list) {
  el.cities.innerHTML = '';
  for (const c of list) {
    try {
      const geo = await geocode(c);
      const wx  = await getWeather(geo.lat, geo.lon, geo.timezone);
      const curr = wx.current;
      const info = wmoInfo(curr.weather_code);
      const card = document.createElement('div');
      card.className = 'city-card';
      card.innerHTML = `
        <div class="city-info">
          <span class="city-temp">${fmtTemp(curr.temperature_2m)}</span>
          <span class="city-name">${geo.name}</span>
          <span class="city-country">${geo.country}</span>
        </div>
        <div class="city-icon">
          <img src="${IMG}${info.icon}@2x.png" alt="${info.label}" />
        </div>
      `;
      card.addEventListener('click', () => {
        el.search.value = geo.name;
        fetchCity(geo.name);
      });
      el.cities.appendChild(card);
    } catch (e) {
      console.warn('City failed:', c);
    }
  }
}

// events //
el.searchBtn.addEventListener('click', () => {
  const q = el.search.value.trim();
  if (q) fetchCity(q);
  else toast('Please enter a city name', 'error');
});

el.search.addEventListener('keydown', e => {
  if (e.key === 'Enter') el.searchBtn.click();
});

el.cBtn.addEventListener('click', () => {
  if (unit === 'celsius') return;
  unit = 'celsius';
  el.cBtn.classList.add('active');
  el.fBtn.classList.remove('active');
  fetchCity(cityName);
  loadCities(showingAll ? allCities : defaultCities);
});

el.fBtn.addEventListener('click', () => {
  if (unit === 'fahrenheit') return;
  unit = 'fahrenheit';
  el.fBtn.classList.add('active');
  el.cBtn.classList.remove('active');
  fetchCity(cityName);
  loadCities(showingAll ? allCities : defaultCities);
});

el.tabDay.addEventListener('click', () => {
  weekMode = false;
  el.tabDay.classList.add('active');
  el.tabWeek.classList.remove('active');
  fetchCity(cityName);
});

el.tabWeek.addEventListener('click', () => {
  weekMode = true;
  el.tabWeek.classList.add('active');
  el.tabDay.classList.remove('active');
  fetchCity(cityName);
});

el.seeAll.addEventListener('click', () => {
  showingAll = !showingAll;
  el.seeAll.textContent = showingAll ? 'Show Less' : 'See All';
  loadCities(showingAll ? allCities : defaultCities);
});

document.querySelectorAll('.nav-btn').forEach(btn => {
  btn.addEventListener('click', function () {
    document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
    this.classList.add('active');
  });
});

// start — no API key needed, works immediately //
fetchCity(cityName);
loadCities(defaultCities);