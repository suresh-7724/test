function delayedSuccess() {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve("Success");
    }, 1000);
  });
}

delayedSuccess().then(console.log); // Logs "Success" after 1 second

