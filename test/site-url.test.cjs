const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const source = fs.readFileSync(path.join(__dirname, '../assets/js/site.js'), 'utf8');
const data = JSON.stringify({ apps: { valid: {
  name: 'Example App', status: 'ok', developer: { value: 'Example Studio' },
  email: { value: '' }, description: { en: 'Example description' }
} } });

function load(appId) {
  const title = { textContent: '' };
  const body = { innerHTML: '' };
  const close = { addEventListener() {}, focus() {} };
  const modal = {
    open: false,
    querySelector: selector => ({ '#modal-title': title, '.modal-body': body, '.modal-close': close })[selector],
    addEventListener() {},
    showModal() { this.open = true; }
  };
  const button = {
    appId: 'valid',
    getAttribute() { return this.appId; },
    setAttribute() {},
    addEventListener(type, listener) { this[type] = listener; },
    focus() {}
  };
  const input = { value: '', addEventListener() {} };
  const clear = { hidden: true, addEventListener() {} };
  const box = { hidden: true, querySelector: selector => selector === 'input' ? input : clear };
  const count = { textContent: '' };
  const empty = { hidden: true };
  const row = { hidden: false, children: [{ textContent: 'Example App', querySelector: () => button }] };
  const table = { parentNode: { hidden: false }, querySelectorAll: () => [row] };
  const elements = {
    'apps-data': { textContent: data }, 'app-modal': modal, 'app-search': box,
    'apps-table': table, 'search-count': count, 'search-empty': empty
  };
  const document = {
    documentElement: {},
    querySelector: selector => selector === '.app-open[data-app="valid"]' ? button : null,
    querySelectorAll: selector => selector === '.app-open' ? [button] : [],
    getElementById: id => elements[id] || null,
    addEventListener() {}
  };
  vm.runInNewContext(source, {
    document, URL, URLSearchParams,
    location: { search: '?app=' + encodeURIComponent(appId) + '&q=Example' },
    window: { I18N: { found_all: 'All {n}', found_one: 'One match', found_many: '{n} matches' } }
  }, { filename: 'site.js' });
  return { modal, title, body, button, box, count, row };
}

for (const id of ['unknown-app', 'constructor', '__proto__', 'toString']) {
  let page;
  assert.doesNotThrow(() => { page = load(id); }, '?app=' + id);
  assert.equal(page.modal.open, false, id + ' must not open a modal');
  assert.equal(page.box.hidden, false, id + ' must allow search initialization');
  assert.equal(page.count.textContent, 'One match');
  assert.equal(page.row.hidden, false);
  page.button.appId = id;
  assert.doesNotThrow(() => page.button.click(), 'button data-app=' + id);
  assert.equal(page.modal.open, false);
}

const page = load('valid');
assert.equal(page.modal.open, true);
assert.equal(page.title.textContent, 'Example App');
assert.match(page.body.innerHTML, /Example Studio/);
assert.equal(page.count.textContent, 'One match');
console.log('PASS site URL guard: unknown and inherited IDs, both callers, valid app, search initialization');
