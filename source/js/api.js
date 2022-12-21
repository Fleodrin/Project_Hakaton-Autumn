const getData = () => {
  fetch('http://127.0.0.1:8000/general/getdata')
    .then((ads) => {
      console.log(ads.content);
    })
    .catch(() => {

      console.log('onFail(): 123');
    });
};

getData();
