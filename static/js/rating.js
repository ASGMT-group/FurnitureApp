document.addEventListener('DOMContentLoaded', function() {
    const ratingDiv = document.querySelector('.rating');
    const stars = ratingDiv.querySelectorAll('.star');
    const currentRating = parseInt(ratingDiv.dataset.rating);

    // Initialize the star ratings
    updateRatingDisplay(currentRating);

    stars.forEach(star => {
        star.addEventListener('click', function() {
            const selectedRating = parseInt(this.dataset.rating);
            updateRating(selectedRating);
        });
    });

    function updateRating(newRating) {
        // Send the new rating to the server using AJAX
        fetch(`/update_rating/${item.id}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ rate: newRating })
        })
        .then(response => response.json())
        .then(data => {
            // Update the rating display
            updateRatingDisplay(newRating);
        })
        .catch(error => {
            console.error('Error updating rating:', error);
        });
    }

    function updateRatingDisplay(newRating) {
        // Update the star icons to reflect the new rating
        stars.forEach(star => {
            const starIcon = star.querySelector('i');
            if (parseInt(star.dataset.rating) <= newRating) {
                starIcon.classList.remove('far');
                starIcon.classList.add('fas');
            } else {
                starIcon.classList.remove('fas');
                starIcon.classList.add('far');
            }
        });
        // Update the rating in the HTML
        ratingDiv.dataset.rating = newRating;
    }

    function getCookie(name) {
        // Helper function to get the CSRF token from the cookie
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});