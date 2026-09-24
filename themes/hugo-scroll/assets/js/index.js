/**
 * Scroll behaviour for the scrolling pages (layouts/_default/scroll.html):
 * - hide the side menu while the cover is in view
 * - highlight the menu item of the section at the top of the window
 *   (the last item once the page is scrolled to the bottom)
 * - fade out the triangle above the section in view
 * Fading is done in CSS (.fixed-nav.is-visible, .post-after.is-hidden).
 */
(function () {
  "use strict";

  var sitehead = document.getElementById("site-head");
  var fnav = document.querySelector(".fixed-nav");
  if (!sitehead || !fnav) return;

  var posts = document.querySelectorAll(".post");
  var items = fnav.querySelectorAll(".fn-item");
  var footer = document.querySelector(".site-footer");

  function pageTop(el) {
    return el.getBoundingClientRect().top + window.scrollY;
  }

  // Height without padding, like jQuery's .height()
  function contentHeight(el) {
    var cs = getComputedStyle(el);
    return el.clientHeight - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);
  }

  function update() {
    var w = window.scrollY;
    var headTop = pageTop(sitehead);
    var headBottom = headTop + contentHeight(sitehead) - 100;
    var onCover = w >= Math.floor(headTop) && w <= Math.ceil(headBottom);
    fnav.classList.toggle("is-visible", !onCover);

    var root = document.documentElement;
    var atBottom = root.clientHeight + w > root.scrollHeight - (footer ? contentHeight(footer) : 0);

    for (var i = 0; i < posts.length; i++) {
      var item = items[i];
      if (!item) continue;

      if (atBottom) {
        item.classList.toggle("active", i === posts.length - 1);
        continue;
      }

      var top = pageTop(posts[i]);
      var inView = w >= top && w <= top + contentHeight(posts[i]);
      item.classList.toggle("active", inView);

      // The triangle at the bottom of the previous section
      var prev = posts[i].parentElement.previousElementSibling;
      var after = prev && prev.classList.contains("post-holder") ? prev.querySelector(".post-after") : null;
      if (after) after.classList.toggle("is-hidden", inView);
    }
  }

  var pending = false;
  window.addEventListener("scroll", function () {
    if (pending) return;
    pending = true;
    window.requestAnimationFrame(function () {
      pending = false;
      update();
    });
  }, { passive: true });

  update();
})();
