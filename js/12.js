
  window.CC.Class.Analytics = new window.Analytics({
    url: "",
    indexes: {"weekly":"2023_02_19","monthly":"2023_02"},
    trackImpressions: true,
    globalProps: {"abTests":[],"deviceType":"desktop","page":"home","user":[],"metadata":[],"original_referer":"direct","created":"2023-02-24T19:12:26+00:00","referrer_info":{"referrer":null,"source":null,"term":null,"medium":null},"locationDetails":{"country":{"iso_code":"US","name":"United States"},"city":{"name":null},"location":{"accuracy_radius":1000,"latitude":37.751,"longitude":-97.822,"time_zone":"America\/Chicago"}},"user_agent":{"browser":{"family":"Chrome","major":"110","minor":"0","patch":"0"},"os":{"family":"Mac","major":"10","minor":"15","patch":"7","nickname":""},"device":{"type":"desktop","family":"Apple"}}}
  });

  CC.track = window.CC.Class.Analytics.track.bind(window.CC.Class.Analytics);
  CC.trackGA = window.CC.Class.Analytics.trackGA.bind(window.CC.Class.Analytics);
