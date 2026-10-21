(function(){
  var root=document.documentElement;
  // Theme toggle (persists in localStorage, falls back to prefers-color-scheme)
  var btn=document.querySelector('.theme-toggle');
  function effective(){var a=root.getAttribute('data-theme');if(a)return a;return matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';}
  function syncBtn(){if(btn)btn.setAttribute('aria-pressed',effective()==='dark'?'true':'false');}
  if(btn){btn.addEventListener('click',function(){var n=effective()==='dark'?'light':'dark';root.setAttribute('data-theme',n);try{localStorage.setItem('theme',n);}catch(e){}syncBtn();});syncBtn();}

  // Wrap tables for horizontal scroll; tracker tables become cards on mobile
  var isTracker=!!document.querySelector('.page-tracker');
  document.querySelectorAll('.content table').forEach(function(t){
    var w=document.createElement('div');w.className='table-wrap';
    var heads=[].map.call(t.querySelectorAll('thead th'),function(th){return th.textContent.trim();});
    if(isTracker&&heads.length>=4){w.className+=' cards';t.querySelectorAll('tbody tr').forEach(function(tr){[].forEach.call(tr.children,function(td,i){td.setAttribute('data-label',heads[i]||'');});});}
    t.parentNode.insertBefore(w,t);w.appendChild(t);
  });

  // Checklist: interactive checkboxes, state in localStorage (this browser only)
  var items=document.querySelectorAll('.content li.task-list-item');
  if(items.length){
    var key='checklist:'+location.pathname;var state={};
    try{state=JSON.parse(localStorage.getItem(key)||'{}');}catch(e){}
    var bar=document.createElement('div');bar.className='checklist-bar';
    bar.innerHTML='<span class="count" aria-live="polite"></span><span class="progress" aria-hidden="true"><i></i></span><button type="button" class="button button-ghost">'+(window.I18N&&I18N.reset||'Reset')+'</button>';
    var content=document.querySelector('.content');content.insertBefore(bar,content.firstChild);
    function update(){var d=0;items.forEach(function(li){if(li.querySelector('input').checked)d++;});bar.querySelector('.count').textContent=d+' / '+items.length+' '+(window.I18N&&I18N.progress||'done');bar.querySelector('.progress i').style.width=(100*d/items.length)+'%';}
    items.forEach(function(li,i){
      var cb=li.querySelector('input[type=checkbox]');if(!cb)return;
      cb.disabled=false;cb.removeAttribute('disabled');cb.id='chk-'+i;
      var label=document.createElement('label');label.setAttribute('for',cb.id);
      var span=document.createElement('span');span.className='t';
      while(li.firstChild){ if(li.firstChild===cb){li.removeChild(cb);continue;} span.appendChild(li.firstChild);}
      label.appendChild(cb);label.appendChild(span);li.appendChild(label);
      cb.checked=!!state[i];li.classList.toggle('done',cb.checked);
      cb.addEventListener('change',function(){state[i]=cb.checked;li.classList.toggle('done',cb.checked);try{localStorage.setItem(key,JSON.stringify(state));}catch(e){}update();});
    });
    bar.querySelector('button').addEventListener('click',function(){state={};try{localStorage.removeItem(key);}catch(e){}items.forEach(function(li){var c=li.querySelector('input');c.checked=false;li.classList.remove('done');});update();});
    update();
  }
  // Tracker: app details modal and live search
  var dataEl=document.getElementById('apps-data');
  var APPS=dataEl?(JSON.parse(dataEl.textContent).apps||{}):{};
  var T=window.I18N||{};var L=T.lang==='uk'?'uk':'en';
  function esc(x){return String(x).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
  function host(u){try{return new URL(u).hostname.replace(/^www\./,'');}catch(e){return u;}}
  function fmtDate(d){if(!d)return'';var p=d.split('-');if(L==='uk')return p.length===3?p[2]+'.'+p[1]+'.'+p[0]:(p[1]?p[1]+'.'+p[0]:p[0]);var m=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];return p.length===3?(+p[2])+' '+m[+p[1]-1]+' '+p[0]:(p[1]?m[+p[1]-1]+' '+p[0]:p[0]);}
  function src(f){if(!f||!f.source)return'';return '<div class="field-src">'+esc(T.m_source)+': <a href="'+esc(f.source)+'" rel="noopener noreferrer" target="_blank">'+esc(host(f.source))+'</a> · '+esc(T.m_checked)+' '+esc(fmtDate(f.checked))+'</div>';}
  function tag(f,has){if(!has)return'<span class="tag tag-none">'+esc(T.m_nodata)+'</span>';if(f.verified===false)return' <span class="tag tag-unv">'+esc(T.m_unverified)+'</span>';return'';}
  function field(label,f,html){var has=!!html;return '<div class="field"><dt>'+esc(label)+'</dt><dd>'+(has?html:'')+tag(f,has)+src(f)+'</dd></div>';}
  var modal=document.getElementById('app-modal');var opener=null;
  function openApp(id,btn){
    var a=Object.prototype.hasOwnProperty.call(APPS,id)?APPS[id]:null;if(!a||!modal)return;opener=btn;
    modal.querySelector('#modal-title').textContent=a.name;
    var h='<div class="modal-status"><span class="badge badge-'+a.status+'">'+esc(T['s_'+a.status])+'</span></div><dl class="fields">';
    h+=field(T.m_developer,a.developer,a.developer.value?esc(a.developer.value):'');
    h+=field(T.m_email,a.email,a.email.value?'<a href="mailto:'+esc(a.email.value)+'">'+esc(a.email.value)+'</a>':'');
    h+=field(T.m_desc,a.description,a.description[L]?esc(a.description[L]):'');
    h+='</dl><h3 class="modal-sub">'+esc(T.m_timeline)+'</h3><ol class="timeline">';
    (a.timeline||[]).forEach(function(e){h+='<li><time datetime="'+esc(e.date)+'">'+esc(fmtDate(e.date))+'</time><p>'+esc(e[L])+'</p>'+(e.source?'<a class="tl-src" href="'+esc(e.source)+'" rel="noopener noreferrer" target="_blank">'+esc(host(e.source))+'</a>':'')+'</li>';});
    h+='</ol><p class="modal-note">'+esc(T.m_note)+'</p>';
    modal.querySelector('.modal-body').innerHTML=h;
    if(modal.showModal)modal.showModal();else modal.setAttribute('open','');
    modal.querySelector('.modal-close').focus();
  }
  if(modal){
    modal.querySelector('.modal-close').addEventListener('click',function(){modal.close();});
    modal.addEventListener('click',function(e){if(e.target===modal)modal.close();});
    modal.addEventListener('close',function(){if(opener)opener.focus();});
    document.querySelectorAll('.app-open').forEach(function(b){b.setAttribute('aria-haspopup','dialog');b.addEventListener('click',function(){openApp(b.getAttribute('data-app'),b);});});
    var mid=new URLSearchParams(location.search).get('app');if(mid&&APPS[mid])openApp(mid,document.querySelector('.app-open[data-app="'+mid+'"]'));
  }

  var box=document.getElementById('app-search');var table=document.getElementById('apps-table');
  if(box&&table){
    box.hidden=false;
    var q=box.querySelector('input');var clr=box.querySelector('.search-clear');
    var count=document.getElementById('search-count');var empty=document.getElementById('search-empty');
    var rows=[].slice.call(table.querySelectorAll('tbody tr'));
    function norm(x){return (x||'').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().replace(/\s+/g,' ').trim();}
    var hay=rows.map(function(tr){var c=tr.children[0];var b=c.querySelector('.app-open');var t=c.textContent;if(b){var a=APPS[b.getAttribute('data-app')];if(a){t+=' '+a.name+' '+(a.developer.value||'');}}return norm(t);});
    function run(push){
      var v=norm(q.value);var n=0;
      rows.forEach(function(tr,i){var ok=!v||hay[i].indexOf(v)>-1;tr.hidden=!ok;if(ok)n++;});
      clr.hidden=!q.value;empty.hidden=n>0;
      count.textContent=!v?T.found_all.replace('{n}',rows.length):(n===1?T.found_one:T.found_many.replace('{n}',n));
      table.parentNode.hidden=n===0;
      if(push){var u=new URL(location.href);if(q.value)u.searchParams.set('q',q.value);else u.searchParams.delete('q');history.replaceState(null,'',u);}
    }
    q.addEventListener('input',function(){run(true);});
    q.addEventListener('keydown',function(e){if(e.key==='Escape'&&q.value){q.value='';run(true);e.stopPropagation();}});
    clr.addEventListener('click',function(){q.value='';run(true);q.focus();});
    document.addEventListener('keydown',function(e){if(e.key==='/'&&!e.ctrlKey&&!e.metaKey&&!e.altKey){var el=document.activeElement;if(el&&(/^(INPUT|TEXTAREA|SELECT)$/.test(el.tagName)||el.isContentEditable))return;if(modal&&modal.open)return;e.preventDefault();q.focus();q.select();}});
    var init=new URLSearchParams(location.search).get('q');if(init)q.value=init;
    run(false);
  }
})();
