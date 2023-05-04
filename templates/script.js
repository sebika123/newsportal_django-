<script>
    $(document).ready(function() {
        $('.like-btn').click(function() {
            var articleId = $(this).data('article-id');
            $.ajax({
                method: 'POST',
                url: '/likes/create/' + articleId + '/',
                success: function(data) {
                    $('.like-count[data-article-id="' + articleId + '"]').text(data.like_count);
                }
            });
        });
    });
</script>