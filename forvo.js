const {
  Builder,
  By,
  Key,
  until,
  size,
  actions,
} = require('selenium-webdriver');
const firefox = require('selenium-webdriver/firefox');
const options = new firefox.Options();

options.setPreference('browser.download.dir', '/Downloads');
options.setPreference('browser.download.folderList', 2);
options.setPreference(
  'browser.helperApps.neverAsk.saveToDisk',
  'application/audio/mpeg'
);

const driver = new Builder()
  .forBrowser('firefox')
  .setFirefoxOptions(options)
  .build();

// (async function() {
// await driver.get("https://forvo.com/download/mp3/any/en/2162053");
// await driver.quit();
// })();

var details = ['', ''];

var keywords = [
  'a',
  'abandon',
  'ability',
  'able',
  'abortion',
  'about',
  'above',
  'abroad',
  'absence',
  'absolute',
  'absolutely',
  'absorb',
  'abuse',
  'academic',
  'accept',
  'access',
  'accident',
  'accompany',
  'accomplish',
  'according',
  'account',
  'accurate',
  'accuse',
  'achieve',
  'achievement',
  'acid',
  'acknowledge',
  'acquire',
  'across',
  'act',
  'action',
  'active',
  'activist',
  'activity',
  'actor',
  'actress',
  'actual',
  'actually',
  'ad',
  'adapt',
  'add',
  'addition',
  'additional',
  'address',
  'adequate',
  'adjust',
  'adjustment',
  'administration',
];

proList = [];

notCatched = [];

(async function () {
  //log in into the website
  await login();

  //navigate to website
  await navigate();

  async function login() {
    await driver.get('https://forvo.com/login/');
    // let logIn = await driver.findElement(By.css('.login'));
    // await logIn.click();
    await driver.sleep(2000);
    let username = await driver.findElement(By.css('#login'));
    await username.click();
    await driver.sleep(200);
    await username.sendKeys(details[0]);
    let password = await driver.findElement(By.css('#password'));
    await password.click();
    await driver.sleep(200);
    await password.sendKeys(details[1]);
    await driver.findElement(By.css('.button')).click();
  }

  async function navigate() {
    for (i = 0; i < keywords.length; i++) {
      await driver.get('https://forvo.com/search/' + keywords[i] + '/en_uk/');
      await driver.sleep(1000);

      // download the file with pronounciation to Downloads folder and push spelling to array proList
      await clickDownloadFileAndSpelling();
      console.log(proList);
    }
    console.log(proList, notCatched);
    console.log(proList.length, keywords.length, notCatched.length);
  }

  async function clickDownloadFileAndSpelling() {
    try {
      let word = await driver.findElement(
        By.css(
          'ul.word-play-list-icon-size-l:nth-child(1) > li:nth-child(1) > a:nth-child(2)'
        )
      );
      await word.click();
      let pronounciation = await driver.findElement(By.css('.phonetics'));
      await pronounciation.getText().then(function (txt) {
        proList.push(` ${txt} `);
      });
      let sweet = await driver.findElement(
        By.xpath("//*[@id='en_uk']/following-sibling::*/div/div/p[3]")
      );
      await sweet.click();
    } catch {
      proList.push('NOT FOUND');
      notCatched.push(keywords[i]);
      console.log(notCatched);
      console.log(i);
    }
  }

  await driver.quit();
})();
