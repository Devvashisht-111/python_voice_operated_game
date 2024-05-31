import puppeteer from "puppeteer";

const automate = async () => {
    const browser = await puppeteer.launch({
        headless: false,
        defaultViewport: null,
        args: ["--start-maximized", "--use-fake-ui-for-media-stream"],
        permissions: ["microphone"],
    });
    console.log("Browser opened");

    const page = await browser.newPage();
    console.log("Page opened");
    await page.goto("http://127.0.0.1:5500/index.html");
    console.log("Page loaded");

    await page.setViewport({ width: 1920, height: 1080 });
    console.log("Page maximized");

    await page.waitForSelector("#start");
    console.log("Start button found");
    await page.click("#start");
    console.log("Start button clicked");

    while (true) {
        try {
            const text = await page.evaluate(() => {
                const outputElement = document.getElementById("output");
                return outputElement ? outputElement.innerText : "";
            });

            if (text) {
                console.log(text);
                const words = text.split(" ");
                for (const word of words) {
                    if (word.includes("left")) {
                        await page.keyboard.press("ArrowLeft");
                    } else if (word.includes("right")) {
                        await page.keyboard.press("ArrowRight");
                    }
                }
            }
        } catch (error) {
            console.error("Error:", error);
        }
    }
};

automate();
