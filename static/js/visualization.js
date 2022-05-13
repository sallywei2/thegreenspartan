

// dataset:
// time,Year,Month,country,countryid,latitude,longitude,population,Area (sq. mi.),gdp,Annual_CO2_emissions,Monthly,Annual,Five-year,Ten-year

function visualization(dataset){

	const ctx = document.getElementById('temperatureChart')
	// .getContext('2d');

	console.log(Object.values(dataset.date))

	const data = {
	  labels: Object.values(dataset.date),
	  datasets: [{
	    label: 'Annual Average Ground Temperature',
	    data: Object.values(dataset.value),
	    fill: false,
	    borderColor: 'rgb(75, 192, 192)',
	    tension: 0.01
	  }]
	};

	const config = {
  	type: 'line',
  	data: data,
  	options: {
  			interaction: {
  				intersect: false,
  				axis: 'xy',
  				mode: 'nearest',
  			}
    },
    plugins: {
      title: {
        display: true,
        text: (ctx) => {
          const {axis = 'xy', intersect, mode} = ctx.chart.options.interaction;
          return 'Mode: ' + mode + ', axis: ' + axis + ', intersect: ' + intersect;
        }
      }
		}
	}

	const myChart = new Chart(ctx, config);
}
