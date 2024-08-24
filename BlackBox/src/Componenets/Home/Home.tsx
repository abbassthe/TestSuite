import { useEffect } from "react";
import "./Home.scss";
function Home() {
  useEffect(() => {
    const script = document.createElement("script");

    script.src = "./script.js";
    script.async = true;
    script.defer = true;
    document.body.appendChild(script);
  }, []);
  const handleParseHtml = () => {
    // Function to parse and log the content
    const parseHtmlContent = () => {
      const lines = document.querySelectorAll(".ace_line");
      lines.forEach((line) => {
        console.log(line.textContent?.trim());
      });
      const output = document.querySelector("#result");
      console.log(output?.textContent?.trim())
    };
    parseHtmlContent();
  };
  useEffect(() => {
    const intervalId = setInterval(() => {
      const button = document.querySelector(".ck-button.run-button");
      if (button) {
        button.addEventListener("click", handleParseHtml);
        clearInterval(intervalId); // Stop polling once the button is found
      }
    }, 1000); // Check every second

    return () => clearInterval(intervalId); // Clean up the interval on component unmount
  }, []);
  return (
    <div className="Wrapper">
      <code-runner
        language="python"
        style={{
          display: "block",
          width: "50%",
          marginLeft: "25%",
          marginTop: "4%",
        }}
      ></code-runner>
      <div className="OutputWrapper">
        <div className="table">abbass \n naim  </div>
        <div className="table">World</div>
      </div>
    </div>
  );
}

export default Home;
