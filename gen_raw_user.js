const instaTouch = require("instatouch");

(async () => {
  try {
    const POST = "https://www.instagram.com/p/CIvLPrylfPi";
    const SESSION_ID = "";
    const NUMBER = 200;
    const FILE_NAME = "user_raw";
    const FILE_PATH = "/home/eagle/d/myapp/cassinelli/dir-spam-bot";
    const FILE_TYPE = "json";

    const options = {
      count: NUMBER,
      session: SESSION_ID,
      filetype: FILE_TYPE,
      filename: FILE_NAME,
      filepath: FILE_PATH,
    };
    instaTouch.likers(POST, options);
  } catch (error) {
    console.log(error);
  }
})();
