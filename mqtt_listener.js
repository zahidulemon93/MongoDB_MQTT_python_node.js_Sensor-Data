var mqtt = require('mqtt'), url = require('url');

var client = mqtt.connect('mqtt://iot.eclipse.org', {
    will: {
        topic: 'imran',
        },
        clientID: 'f6c63264-99d0-4fa3-a0eb-0358a8eb1b67'
});

client.on('connect', function () { // When connected

    // subscribe to a topic

    client.subscribe('imran', function () 
    {
        // when a message arrives, do something with it

        client.on('message', function (topic, message, packet) {

            console.log("Received '" + message + "' on '" + topic + "'");

           // set the temperature. 

        });

    });

});