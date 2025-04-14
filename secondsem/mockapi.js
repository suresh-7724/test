async function fetchMockData() {
  const data = await new Promise(resolve => {
    setTimeout(() => {
      resolve({ message: "Mock API Data" });
    }, 1500);
  });

  console.log(data); // { message: "Mock API Data" }
}

fetchMockData();
