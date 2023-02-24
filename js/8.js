
  CC.data = CC.data || {};
  CC.data.notifications = [];
  window.TOUCHSCREEN = false;
  window.addEventListener("touchstart", () => {
    document.body.classList.add("touch");
    window.TOUCHSCREEN = true;
  });
  window.EXTRACT_URL = "https://us-central1-class-central-prod.cloudfunctions.net/extract";
