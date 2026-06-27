
        // Simple micro-interaction for form validation visual feedback
        document.querySelector('form').addEventListener('submit', (e) => {
            const pwd = document.getElementById('password').value;
            const pwdCheck = document.getElementById('password_check').value;
            
            if (pwd !== pwdCheck) {
                e.preventDefault();
                alert('Passwords do not match');
                document.getElementById('password_check').classList.add('border-error');
            }
        });

        // Reset error style on input
        document.getElementById('password_check').addEventListener('input', function() {
            this.classList.remove('border-error');
        });
