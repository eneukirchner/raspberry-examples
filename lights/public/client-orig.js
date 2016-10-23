$(document).ready(function(){
    
    var colors = { r:"0", g:"0", b:"0"};
    
    // WebSocket
    var socket = io.connect();
   
    // neue Nachricht
    socket.on('chat', function(data) {
        colors = data;
        // alert(data.r + ' ' + data.g + ' ' + data.b);
        // $('#content').append(colors.r + ' ' + colors.g + ' ' + colors.b + "***");
        $("#red").val(colors.r).slider('refresh');
        $("#green").val(colors.g).slider('refresh');
        $("#blue").val(colors.b).slider('refresh');
    });
    
    
    
    $('#red').on('slidestop',function( event ){
        colors.r = $("#red").val();
        socket.emit('chat', colors);
    });
    
    $('#green').on('slidestop',function( event ){
        colors.g = $("#green").val();
        socket.emit('chat', colors);
    });

    $('#blue').on('slidestop',function( event ){
        colors.b = $("#blue").val();
        socket.emit('chat', colors);
    });

});


      
