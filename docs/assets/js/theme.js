(function () {
  const STORAGE_KEY = "theme";
  const DARK = "dark";
  const LIGHT = "light";

  function parse(value) {
    return value === DARK || value === LIGHT ? value : null;
  }

  function readStored() {
    try {
      return parse(localStorage.getItem(STORAGE_KEY));
    } catch (_) {
      return null;
    }
  }

  function store(theme) {
    try {
      localStorage.setItem(STORAGE_KEY, theme);
    } catch (_) {}
  }

  function systemTheme() {
    try {
      return window.matchMedia("(prefers-color-scheme: dark)").matches
        ? DARK
        : LIGHT;
    } catch (_) {
      return LIGHT;
    }
  }

  function resolve() {
    return readStored() || systemTheme();
  }

  function apply(theme) {
    const html = document.documentElement;
    html.classList.toggle(DARK, theme === DARK);
    html.classList.toggle(LIGHT, theme === LIGHT);
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) {
      meta.setAttribute(
        "content",
        theme === DARK ? meta.dataset.dark : meta.dataset.light
      );
    }
  }

  let current = parse(window.__initialTheme) || resolve();
  apply(current);

  function toggle() {
    current = current === DARK ? LIGHT : DARK;
    store(current);
    apply(current);
    return current;
  }

  window.toggleTheme = toggle;

  document.addEventListener("DOMContentLoaded", function () {
    apply(current);
    document.querySelectorAll("[data-theme-toggle]").forEach(function (btn) {
      btn.addEventListener("click", function (e) {
        e.preventDefault();
        toggle();
      });
    });
  });

  const mql =
    typeof window.matchMedia === "function"
      ? window.matchMedia("(prefers-color-scheme: dark)")
      : null;
  if (mql && mql.addEventListener) {
    mql.addEventListener("change", function (e) {
      if (readStored()) return;
      current = e.matches ? DARK : LIGHT;
      apply(current);
    });
  }

  document.addEventListener("keydown", function (e) {
    if (e.key === "F1") {
      e.preventDefault();
      toggle();
    }
  });
})();
