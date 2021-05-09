// argv[2]: url
// argv[3]: timeout

argv = process.argv;
console.log("***********************************i am in**********************************")
const CDP = require('chrome-remote-interface');

function sleep(time = 0) {
	return new Promise((resolve, reject) => {
		setTimeout(() => {
			resolve();
		}, time);
	});
}

async function example() {
	let client;

	var in_url = argv[2];
	var in_timeout = parseInt(argv[3]);

	try {
		// connect to endpoint
		client = await CDP();
		// extract domains
		const {Network, Page, Runtime, Target} = client;

		async function invoke(in_expression, success_function, time_to_sleep = 0) {
			startTime = process.uptime();
			result = await Runtime.evaluate({expression: in_expression});
			console.log(result);
			while (!success_function()) {
				curTime = process.uptime();
				if (curTime - startTime > in_timeout) {
					console.log(">>> TimeOut ");
					break;
				}
				if(time_to_sleep > 0) {
				    await sleep(time_to_sleep*1000)
				}
				result = await Runtime.evaluate({expression: in_expression});
				console.log(result);
			}
		}

		// setup handlers
		// Network.requestWillBeSent((params) => {
		// 	console.log(params.request.url);
		// });
		// enable events then start!
		await Network.enable();
		await Page.enable();
		await Page.navigate({url: in_url});
		//await Page.loadEventFired();
			result = await Runtime.evaluate({expression: 'document.readyState'});
		//console.log(result);
		while (result.result.value == "loading") {
			result = await Runtime.evaluate({expression: 'document.readyState'});
		}
		startTime = process.uptime();
		while (result.result.value != "complete") {
			curTime = process.uptime();
			if (curTime - startTime > in_timeout) {
				console.log(">>> TimeOut ");
				break;
			}
			result = await Runtime.evaluate({expression: 'document.readyState'});
			console.log(result);
		}
		console.log(result);

        // wait the page
        await invoke(
            'window.finishFlag',
            function() {return result.result.value == "finished"},
            2);

        result = await Runtime.evaluate({
            expression: 'window.timeUsage_'
        });

        console.log("DONE FOR RUNNING 3RD LIBRARY. TIME USAGE is " + result.result.value);

        sleep(2000);

	} catch (err) {
		console.error(err);
	} finally {
		if (client) {
			await client.close();
		}
	}
}


example();
