$(document).ready(function () {

    eel.init()()
    //    for dynamic moving text
    $('.text').textillate({ 
        loop: true,
        speed: 1500,
        sync: true,
        in:{
            effect:"bounceIn",
        },
        out:{
            effect:"bounceOut",
        },

    });
    $('.siri-message').textillate({ 
        loop: true,
        speed: 1500,
        sync: true,
        in:{
            effect:"fadeInUp",
            sync: true,
        },
        out:{
            effect:"fadeOutUp",
            sync: true,
        },

    });

    
    var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 940,
    style: "ios9",
    amplitude: "1",
    speed: "0.30",
    height: 200,
    autostart: true,
    waveColor: "#ff0000",
    waveOffset: 0,
    rippleEffect: true,
    rippleColor: "#ffffff",
    });
    
    // when click the mic button ,the siri wave will start
    $("#MicBtn").click(function () { 
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.play_assistant_sound();
        // eel.takecommand()();
        eel.takeAllCommands()();


    });

    // when tap the ctrl+j button , the jarvis will activate
    function doc_keyUp(e){

        if (e.key === "j" && e.ctrlKey){
            eel.play_assistant_sound()
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.takeAllCommands()();
        }
    }
    document.addEventListener("keyup", doc_keyUp, false);

    function PlayAssistant(message){
        if (message != ""){
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.takeAllCommands(message);
            $("#chatbox").val("")
            $("#MicBtn").attr("hidden", false);
            $("#SendBtn").attr("hidden", true);
        }
    }
    
    function ShowHideButton(message){
        if (message.length == 0){
            $("#MicBtn").attr("hidden", false);
            $("#SendBtn").attr("hidden", true);
        }
        else{
            $("#MicBtn").attr("hidden", true);
            $("#SendBtn").attr("hidden", false);
        }
    }
    $("#chatbox").keyup(function(){
        let message = $("#chatbox").val();
        ShowHideButton(message);
    });
    $("#SendBtn").click(function(){
        let message = $("#chatbox").val();
        PlayAssistant(message);
    });

});



