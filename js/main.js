$(document).ready(function(){
    $('#post_story').click(function(){
        var title = $('#title').val();
        var story = $('#story').val();
        var newDiv = $('<div class="container form-group border rounded-3 px-5 mb-4 bg-light"> <div class="border-bottom h5 mt-3 mb-3">' + title + '</div> <div class="border-bottom"> '+ story +' </div> <div class="mt-3 mb-1" style="width: 200px;"><button type="button" class="btn btn-outline-primary" id="post_story">Post story</button></div></div>');
        $("#storiesContainer").prepend(newDiv).fadeIn('slow');
        $('#title').val('');
        $('#story').val('');
    });
});
