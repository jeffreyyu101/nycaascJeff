		    var ctx = document.getElementById("sourceChart");

		    var data = {
				labels: [
			        "SAB Budget",
			        "Fund 22 Donation",
			        "APA Institute",
			        "AAARI - CUNY",
			        "T-shirt sales"
			    ],

			    datasets: [
			        {
			            data: [4000, 1003, 1500, 250, 57],
			            backgroundColor: [
			                "#CF3339",
			                "#CF3339",
			                "#CF3339",
			                "#CF3339",
			                "#CF3339"
			            ],
			            hoverBackgroundColor: [
			                "#444444",
			                "#444444",
			                "#444444",
			                "#444444",
			                "#444444"
			            ]
			        }]
			};

			var sourceChart = new Chart(ctx, {
			    type: 'pie',
			    data: data,
			    options: {
			    	animation: {
			    		animateScale: true
			    	},

			    	legend: {
			    		position: 'left',
			    		labels: {
						    fontColor: "#444444",
				            fontFamily: "'Roboto', 'Helvetica', sans-serif",
						    boxWidth: 12
    			
			    		}
			    	},

			    	tooltips: {
			    		backgroundColor: 'rgba(255,255,255,0.8)',
			    		bodyFontFamily: "'Roboto', 'Helvetica', sans-serif",
			    		bodyFontSize: 10,
			    		bodyFontColor: "#CF3339",
			    		displayColors: false

			    	}
			    }
			});