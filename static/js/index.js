const urls = [visualizationUrl];

// triggers each of the urls
Promise.all(urls.map(url => d3.json(url))).then(run);

function run(dataset) {
   visualization(dataset[0]);
};