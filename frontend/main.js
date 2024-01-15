const form = document.querySelector("#chat-form");
const chatlog = document.querySelector("#chat-log");
const submit_btn = document.getElementById("submit-btn");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  // Get the user's message from the form
  const message = form.elements.message.value;
  const new_payload = { message: "what is pythogoras theorem", stream: true };

  // Send a request to the Flask server with the user's message
  const response = await fetch(
    "https://pepsi-cog-search-ai-poc-backend.azurewebsites.net/search/gptcall_ext",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(new_payload),
    }
  );

  // const new_payload = { message: "what is pythogoras theorem", stream: true };
  // const response = await fetch("http://127.0.0.1:5000/search/gptcall_ext", {
  //   method: "POST",
  //   body: JSON.stringify(new_payload),
  //   headers: {
  //     "Content-Type": "application/json",
  //   },
  // });

  // Create a new TextDecoder to decode the streamed response text
  const decoder = new TextDecoder();

  // Set up a new ReadableStream to read the response body
  const reader = response.body.getReader();
  let chunks = "";
  let chunk_data = "";
  let chunk_data1 = "";
  // Read the response stream as chunks and append them to the chat log
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    chunk_data = decoder.decode(value);
    chunk_data = chunk_data.replace(/^data: /, "");
    chunks_json = JSON.parse(chunk_data);
    console.log("chunks_json ==>", chunks_json);
    // console.log("dtype : ", typeof chunk_data1);
    // if (chunks_json.hasOwnProperty("data_url")) {
    //   console.log("URl is found : ", chunks_json.data_url);
    // }
    // console.log("This is data : ", chunks_json?.data_url);
    // console.log("This is type of data : ", typeof chunks_json);
    // chatlog.innerHTML = chunks;
  }
});

// submit_btn.addEventListener("click", (e) => {
//   try {
//     const eventSource = new EventSource("http://localhost:5000/"); // Replace with the correct URL of your Flask API
//     eventSource.onmessage = function (event) {
//       const data = JSON.parse(event.data);
//       console.log(data);
//       // Do something with the received data, e.g., update the UI
//     };

//     eventSource.onerror = function (error) {
//       console.error("EventSource failed:");
//       eventSource.close();
//     };
//   } catch {
//     console.log("This is error");
//   }
// });
