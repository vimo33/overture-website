(function () {
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  var nav = document.querySelector("[data-site-nav]");
  var toggle = document.querySelector("[data-nav-toggle]");
  if (nav && toggle) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });

    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  var revealTargets = Array.prototype.slice.call(
    document.querySelectorAll("[data-reveal], [data-stagger]")
  );

  if (!reduceMotion && "IntersectionObserver" in window && revealTargets.length) {
    var revealObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            revealObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.14, rootMargin: "0px 0px -32px 0px" }
    );

    revealTargets.forEach(function (target) {
      revealObserver.observe(target);
    });
  } else {
    revealTargets.forEach(function (target) {
      target.classList.add("is-visible");
    });
  }

  document.querySelectorAll("[data-faq]").forEach(function (item) {
    var button = item.querySelector(".faq-item__button");
    if (!button) return;
    button.addEventListener("click", function () {
      var open = item.classList.toggle("is-open");
      button.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });

  if (!reduceMotion) {
    var parallaxNodes = Array.prototype.slice.call(document.querySelectorAll("[data-parallax]"));
    if (parallaxNodes.length) {
      var latestY = 0;
      var ticking = false;

      var updateParallax = function () {
        parallaxNodes.forEach(function (node) {
          var speed = parseFloat(node.getAttribute("data-parallax")) || 0.08;
          var offset = latestY * speed;
          node.style.transform = "translate3d(0," + offset.toFixed(2) + "px,0)";
        });
        ticking = false;
      };

      window.addEventListener(
        "scroll",
        function () {
          latestY = window.scrollY;
          if (!ticking) {
            window.requestAnimationFrame(updateParallax);
            ticking = true;
          }
        },
        { passive: true }
      );
    }
  }
})();
