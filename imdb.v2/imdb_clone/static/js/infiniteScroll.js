/*
Infinite Scroll v 1.0.6 - minified
https://github.com/marshall-ku/Infinite-Scroll
Released under the MIT License.
by Marshall K
*/

function infiniteScroll({container:e,next:t,prev:r,item:n,nextButton:l,prevButton:o,nextLoader:s,prevLoader:c,pushHistory:i,detectLoad:a,onLoadFinish:u,nextCallback:d,prevCallback:f,autoPrev:y}){const h=window.innerHeight,p=document.querySelector(e),S=document.querySelector(t),v=document.querySelector(r),m={next:s&&document.querySelector(s),prev:c&&document.querySelector(c)},q=[],L="reveal";let g=!1,w=!1,A=window.scrollY||window.pageYOffset,E=!1;function x(){S.classList.add("done"),S.removeAttribute("href"),s&&(m.next.style.display="none"),l&&(l.style.display="none")}function b(){v.classList.add("done"),v.removeAttribute("href"),c&&(m.prev.style.display="none"),o&&(o.style.display="none")}function k(){const e=document.querySelector(t);if(null===e||!0===g||e.classList.contains("done"))return;let r=0,o=0;const c=e.href;g=!0,s&&m.next.classList.add(L),l&&(l.style.display="none"),fetch(c).then(e=>{const t=e.status;if(200===t)return e.text();404===t&&x()}).then(f=>{const y=(new DOMParser).parseFromString(f,"text/html"),h=y.querySelectorAll(n);null===y.querySelector(t)||""===y.querySelector(t).getAttribute("href")?x():e.href=y.querySelector(t).href,h.forEach(e=>{a&&e.querySelectorAll("img").forEach(e=>{r++,e.addEventListener("load",()=>{r===++o&&(i&&history.pushState(null,null,c),s&&m.next.classList.remove(L),l&&!S.classList.contains("done")&&(l.style.display=""),g=!1,u&&u())})}),p.append(e),d&&d(e)}),a||(g=!1,s&&m.next.classList.remove(L),l&&(l.style.display=""))}).catch(e=>{console.log(e)})}function F(){const e=document.querySelector(r);if(null===e||!0===w||e.classList.contains("done"))return;let t=!1,l=0,s=0;const i=e.href,d=()=>{l===s&&(c&&m.prev.classList.remove(L),w=!1,o&&!v.classList.contains("done")&&(o.style.display=""),u&&u())};w=!0,c&&m.prev.classList.add(L),o&&(o.style.display="none"),fetch(i).then(e=>{const r=e.status;return 200===r?e.text():404===r&&(t=!0,b(),!1)}).then(o=>{const i=(new DOMParser).parseFromString(o,"text/html"),u=i.querySelectorAll(n);y&&!t&&(t=null===i.querySelector(r)||""===i.querySelector(r).getAttribute("href")),null===i.querySelector(r)||""===i.querySelector(r).getAttribute("href")?b():e.href=i.querySelector(r).href,y?(t?b():e.href=i.querySelector(r).href,i.querySelectorAll(n).reverse().forEach(e=>{q.push(e)}),t?q.forEach(e=>{a&&e.querySelectorAll("img").forEach(e=>{l++,e.addEventListener("load",()=>{s++,d()})}),p.prepend(e),f&&f(e)}):(w=!1,F())):(u.reverse().forEach(e=>{a&&e.querySelectorAll("img").forEach(e=>{l++,e.addEventListener("load",()=>{s++,d()})}),p.prepend(e),f&&f(e)}),a||(w=!1,c&&m.prev.classList.remove(L)))}).catch(e=>{console.log(e)})}function O(){const e=p.offsetTop;!l&&null!==S&&""!==S.getAttribute("href")&&!g&&A>=e+p.scrollHeight-h-500&&k(),!o&&null!==v&&""!==v.getAttribute("href")&&!w&&A<=e+500&&F()}!function(){if(!e||!t||!n)throw"Initial Elements are Missing!";l&&(l=document.querySelector(l)),o&&(o=document.querySelector(o)),null===S?x():""===S.getAttribute("href")&&x(),null===v?b():""===v.getAttribute("href")&&b(),void 0===a&&(a=!0)}(),!o&&y&&F(),O(),window.addEventListener("scroll",()=>{E||(E=!0,window.requestAnimationFrame(()=>{A=window.scrollY||window.pageYOffset,O(),E=!1}))},{passive:!0}),l&&l.addEventListener("click",()=>{k()}),o&&o.addEventListener("click",()=>{F()})}