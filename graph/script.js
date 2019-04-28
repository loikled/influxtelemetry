"use strict";

const fetchData = () => {
    console.log("fetching data");
    return fetch(`http://localhost:8086/query?db=telemetry&q=SELECT%20"kneePosition"%20FROM%20"motor_positions"`)
      .then( response => {
        if (response.status !== 200) {
          console.log(response);
        }
        return response;
      })
      .then( response => response.json() )
      .then( parsedResponse => {
        const data = [];
        parsedResponse.results[0].series[0].values.map( (elem, i) => {
          let newArr = [];
          newArr.push(new Date(Date.parse(elem[0])));
          newArr.push(elem[1]);
          data.push(newArr);
        });
        console.log("Fetched " + data.length + " elements")
        return data;
      })
      .catch( error => console.log(error) );
  }


  const drawGraph = () => {
    let g;
    Promise.resolve(fetchData())
      .then( data => {
        g = new Dygraph(
          document.getElementById("div_g"),
          data,
          {
            drawPoints: true,
            title: 'Knee position',
            titleHeight: 32,
            ylabel: 'Knee Position',
            xlabel: 'Date',
            strokeWidth: 1.5,
            labels: ['Date', 'Radians'],
          });
      });
  
    // window.setInterval( () => {
    //   console.log(Date.now());
    //   Promise.resolve(fetchData())
    //     .then( data => {
    //       g.updateOptions( { 'file': data } );
    //     });
    // }, 300000);
  }

  // Call the function then the document is ready.
  $(document).ready(drawGraph());
