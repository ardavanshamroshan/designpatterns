(function () {
  function initCompare(root) {
    const tabs = root.querySelectorAll("[data-compare-tab]");
    const panels = root.querySelectorAll("[data-compare-panel]");

    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        const id = tab.getAttribute("data-compare-tab");
        tabs.forEach(function (t) {
          t.setAttribute("aria-selected", String(t === tab));
        });
        panels.forEach(function (panel) {
          panel.classList.toggle(
            "is-active",
            panel.getAttribute("data-compare-panel") === id
          );
        });
      });
    });
  }

  function initSteps(root) {
    root.querySelectorAll("[data-step]").forEach(function (step) {
      const btn = step.querySelector("[data-step-toggle]");
      if (!btn) return;
      btn.addEventListener("click", function () {
        const open = !step.classList.contains("is-open");
        step.classList.toggle("is-open", open);
        btn.setAttribute("aria-expanded", String(open));
      });
    });
  }

  function initQuiz(root) {
    const feedback = root.querySelector("[data-quiz-feedback]");
    const options = root.querySelectorAll("[data-quiz-opt]");
    const answer = root.getAttribute("data-answer");

    options.forEach(function (btn) {
      btn.addEventListener("click", function () {
        if (root.getAttribute("data-done") === "1") return;
        root.setAttribute("data-done", "1");
        const value = btn.getAttribute("data-quiz-opt");
        const correct = value === answer;

        options.forEach(function (opt) {
          opt.disabled = true;
          if (opt.getAttribute("data-quiz-opt") === answer) {
            opt.classList.add("is-correct");
          } else if (opt === btn && !correct) {
            opt.classList.add("is-wrong");
          }
        });

        if (feedback) {
          feedback.classList.toggle("is-ok", correct);
          feedback.classList.toggle("is-no", !correct);
          feedback.textContent = correct
            ? root.getAttribute("data-ok") || "Correct."
            : root.getAttribute("data-no") || "Not quite — try the next lesson tip.";
        }
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("[data-compare]").forEach(initCompare);
    document.querySelectorAll("[data-steps]").forEach(initSteps);
    document.querySelectorAll("[data-quiz]").forEach(initQuiz);
  });
})();
