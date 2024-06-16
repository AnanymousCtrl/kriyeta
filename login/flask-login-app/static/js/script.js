// document.getElementById('registerForm').addEventListener('submit', async (e) => {
//     e.preventDefault();
//     const username = document.getElementById('registerUsername').value;
//     const password = document.getElementById('registerPassword').value;
//     try {
//         const response = await fetch('/api/auth/register', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify({ username, password })
//         });
//         const data = await response.json();
//         alert(data.msg);
//     } catch (err) {
//         console.error(err);
//     }
// });

// document.getElementById('loginForm').addEventListener('submit', async (e) => {
//     e.preventDefault();
//     const username = document.getElementById('loginUsername').value;
//     const password = document.getElementById('loginPassword').value;
//     try {
//         const response = await fetch('/api/auth/login', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify({ username, password })
//         });
//         const data = await response.json();
//         alert(data.msg);
//     } catch (err) {
//         console.error(err);
//     }
// });


$(document).ready(function() {
    const formCollection = $('.form-collection');
    const loginForm = $('#loginForm');
    const registerForm = $('#registerForm');

    loginForm.on('submit', async function(e) {
        e.preventDefault();
        const username = $('#loginUsername').val();
        const password = $('#loginPassword').val();
        try {
            const response = await fetch('/api/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password })
            });
            const data = await response.json();
            alert(data.msg);
        } catch (err) {
            console.error(err);
        }
    });

    registerForm.on('submit', async function(e) {
        e.preventDefault();
        const username = $('#registerUsername').val();
        const password = $('#registerPassword').val();
        try {
            const response = await fetch('/api/auth/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password })
            });
            const data = await response.json();
            alert(data.msg);
        } catch (err) {
            console.error(err);
        }
    });

    $(document).on('click', '.below button', function() {
        let belowCard = $('.below'),
            aboveCard = $('.above'),
            parent = $('.form-collection');
        
        parent.addClass('animation-state-1');
        
        setTimeout(function() {
            belowCard.removeClass('below');
            aboveCard.removeClass('above');
            belowCard.addClass('above');
            aboveCard.addClass('below');
            
            setTimeout(function() {
                parent.addClass('animation-state-finish');
                parent.removeClass('animation-state-1');
                
                setTimeout(function() {
                    aboveCard.addClass('turned');
                    belowCard.removeClass('turned');
                    parent.removeClass('animation-state-finish');
                }, 300);
            }, 10);
        }, 300);
    });
});
