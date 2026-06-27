
        // Micro-interaction: Active state simulation for sidebar
        const navLinks = document.querySelectorAll('aside nav a');
        navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                navLinks.forEach(l => {
                    l.classList.remove('bg-primary-container', 'text-on-primary-container');
                    l.classList.add('text-on-surface-variant');
                });
                link.classList.add('bg-primary-container', 'text-on-primary-container');
                link.classList.remove('text-on-surface-variant');
            });
        });

        // Hover effect for product cards
        const productCards = document.querySelectorAll('.group');
        productCards.forEach(card => {
            card.addEventListener('mouseenter', () => {
                card.style.transform = 'scale(1.02)';
            });
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'scale(1)';
            });
        });

