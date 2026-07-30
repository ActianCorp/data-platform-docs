// Google Analytics 4 (gtag.js) loader.
//
// In the MkDocs Material build this lived in a custom analytics partial
// (theme_overrides/partials/integrations/analytics/custom.html), driven by
// `extra.analytics`. Zensical does not expose that Material-specific partial,
// so page-view tracking is loaded here via `extra_javascript` instead. This is
// standard gtag.js and does not depend on any theme internals.
(function () {
  var GA_MEASUREMENT_ID = "G-NHC5CN295F";

  var s = document.createElement("script");
  s.async = true;
  s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA_MEASUREMENT_ID;
  document.head.appendChild(s);

  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { window.dataLayer.push(arguments); };
  window.gtag("js", new Date());
  window.gtag("config", GA_MEASUREMENT_ID);
})();
