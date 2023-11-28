/*
Autor: microsoftwarelabs
numero de contato no zang: https://services.zangi.com/dl/conversation/1094194496
technical support:https://www.vivaolinux.com.br/~cumestive
Os direitos autorais desse código pertencem à organização microsoftweralabs.
The copyright of this Code belongs to the MicrosoftWeralabs organization.
*/ 

// Import required libraries
const fs = require('fs');
const util = require('util');

// Create a write stream to a log file
const logFile = fs.createWriteStream('log.txt', {flags: 'a'});

// Function to write a chat message to the log file
function writeChatMessage(message) {
    logFile.write(message + '\n');
}

// Function to read chat messages from the log file
function readChatMessages(callback) {
    fs.readFile('log.txt', 'utf8', function(err, data) {
        if (err) {
            return console.log(err);
        }
        var chatHistory = data.split('\n');
        callback(chatHistory);
    });
}

// Example usage
writeChatMessage('Hello, world!');
readChatMessages(function(chatHistory) {
    console.log(chatHistory);
});