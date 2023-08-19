let ead = document.querySelector('#ead');
        let lsm = document.querySelector('#lsm');
        hide()
        document.querySelector('.toggle-switch input').addEventListener('change', e => { 
            lsm.style.display = e.target.checked ? 'block' : 'none';
            ead.style.display = e.target.checked ? 'none' : 'block';
        });