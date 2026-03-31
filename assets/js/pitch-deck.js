(function () {
  var body = document.body;
  if (!body || !body.classList.contains("deck-root")) return;

  var prev = body.getAttribute("data-prev");
  var next = body.getAttribute("data-next");

  function go(url) {
    if (!url) return;
    window.location.href = url;
  }

  document.addEventListener("keydown", function (event) {
    if (event.key === "ArrowRight" || event.key === "PageDown" || event.key === " ") {
      event.preventDefault();
      go(next);
    }
    if (event.key === "ArrowLeft" || event.key === "PageUp") {
      event.preventDefault();
      go(prev);
    }
    if (event.key.toLowerCase() === "h") {
      window.location.href = "./index.html";
    }
  });

  var wheelLocked = false;
  window.addEventListener(
    "wheel",
    function (event) {
      if (wheelLocked) return;
      if (Math.abs(event.deltaY) < 24) return;
      wheelLocked = true;
      window.setTimeout(function () {
        wheelLocked = false;
      }, 500);
      if (event.deltaY > 0) {
        go(next);
      } else {
        go(prev);
      }
    },
    { passive: true }
  );

  document.querySelectorAll("[data-deck-nav]").forEach(function (node) {
    node.addEventListener("click", function () {
      var target = node.getAttribute("data-deck-nav");
      if (target === "prev") go(prev);
      if (target === "next") go(next);
    });
  });
})();
