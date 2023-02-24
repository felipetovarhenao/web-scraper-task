
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
          m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');


          ga('create', 'UA-27280844-1', 'auto');
    ga('create', 'UA-27280844-1', 'auto');
  ga('set', 'anonymizeIp', true);

      ga('send', 'pageview');
  
  function recordOutboundLink(link, initiative, coursename, stream) {
      try {
          ga('send','event', 'Outbound Clicks - Course from Initiative' , initiative, coursename );
          ga('send','event', 'Outbound Clicks - Course from Stream' , stream, coursename );
          window.open(link);
      }catch(err){}
  }

  function recordOutboundLinkWithoutRedirect( initiative, coursename, stream) {
      try {
          ga('send','event', 'Outbound Clicks - Course from Initiative' , initiative, coursename );
          ga('send','event', 'Outbound Clicks - Course from Stream' , stream, coursename );
      }catch(err){}
  }

  function recordInboundLink(link, initiative, coursename, section) {
      try {
          ga('send','event', 'Inbound Clicks - Course from Initiative' , initiative, coursename );
          ga('send','event', 'Inbound Clicks - Course from Section' , section, coursename );
      }catch(err){}
  }

  function recordTaglineClicks(link, initiative) {
      try {
          ga('send','event', 'Tagline Clicks' , initiative );
          window.open(link);
      }catch(err){}
  }
