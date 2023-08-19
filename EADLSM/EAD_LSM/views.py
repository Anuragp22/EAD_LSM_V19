from django.http import HttpResponse
from django.shortcuts import render


def city_list(request):
    cities = [
        {'name': 'Hyderabad'},
        {'name': 'Chennai'},
        {'name': 'Ahmedabad'},
        {'name': 'Aurangabad'},
        {'name': 'Guwahati'},
        {'name': 'Ahmedabad'},
        {'name': 'Noida'},
        {'name': 'Coimbatore'},
        {'name': 'Siliguri'},
        {'name': 'Raipur'},
        {'name': 'Indore'},
        {'name': 'Kanpur'},
        {'name': 'Lucknow'},
        {'name': 'Mumbai'},
        {'name': 'Bhopal'},
        {'name': 'Chandigarh'},
        {'name': 'Patna'},
        {'name': 'Jabalpur'},
        {'name': 'Pune'},
        {'name': 'Nagpur'},
        {'name': 'Pune'},
        {'name': 'Delhi'},
    ]
    context = {'cities': cities}
    return render(request, 'city_list.html', context)


def city_detail(request, city_name):
    city_details={
       'Hyderabad': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Chennai':{'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Ahmedabad': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Aurangabad': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Guwahati': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Noida': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Coimbatore':{'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Siliguri': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Raipur':{'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Indore': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Jamshedpur':{'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Kanpur':{'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Lucknow': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Mumbai': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Bhopal': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Chandigarh':{'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Patna': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Jabalpur': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Pune': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Nagpur': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Praygraj': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Kochi': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Dehradun': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Jaipur':{'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Kolkata': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Ranchi': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Gorakhpur': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},

    }
    selected_city = city_details.get(city_name)
    context = {'city': selected_city, 'city_name': city_name}
    return render(request, 'city_detail.html', context)

def LSM_CITY_LIST(request):
    Lsm_cities = [
        {'name': 'Hyderabad'},
        {'name': 'Chennai'},
        {'name': 'Ahmedabad'},
        {'name': 'Aurangabad'},
        {'name': 'Guwahati'},
        {'name': 'Ahmedabad'},
        {'name': 'Noida'},
        {'name': 'Coimbatore'},
        {'name': 'Siliguri'},
        {'name': 'Raipur'},
        {'name': 'Indore'},
        {'name': 'Kanpur'},
        {'name': 'Lucknow'},
        {'name': 'Mumbai'},
        {'name': 'Bhopal'},
        {'name': 'Chandigarh'},
        {'name': 'Patna'},
        {'name': 'Jabalpur'},
        {'name': 'Pune'},
        {'name': 'Nagpur'},
        {'name': 'Pune'},
        {'name': 'Delhi'},
    ]
    context = {'Lsm_cities': Lsm_cities}
    return render(request, 'LSM_city_list.html', context)


def LSM_CITY_Detail(request, City_name):
    LSM_CITY_DETAIL={
       'Hyderabad': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Chennai':{'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Ahmedabad': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Aurangabad': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Guwahati': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Noida': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Coimbatore':{'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Siliguri': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Raipur':{'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Indore': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Jamshedpur':{'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Kanpur':{'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Lucknow': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Mumbai': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Bhopal': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Chandigarh':{'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Patna': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Jabalpur': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Pune': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Nagpur': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Praygraj': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Kochi': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Dehradun': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Jaipur':{'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Kolkata': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Ranchi': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},
        'Gorakhpur': {'AM_Name': 'a', 'Date':'Coming soon', 'Venue': 'Coming soon','Time':'Coming soon','Testimonail_Name':['Mahendra Surekha', 'Anurag Rastogi', 'Gaurav Agarwal','Mohit Sahu','Anubhav Agarwal'],
            'Images':
            [
                'IMG/EAD_TESTIMONIAL_PHOTOS/mohit-sahu392771250.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/29706437608.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1661579849552.jpeg',
                'IMG/EAD_TESTIMONIAL_PHOTOS/anubhav2.png',
                'IMG/EAD_TESTIMONIAL_PHOTOS/1563187949904.png'
            ],
            'Testimonail_Sentence':
            ['The event was an absolute game-changer! From the inspiring speakers to the engaging workshops, it left me feeling motivated and empowered to take on new challenges',
             'Attending the event was a transformative experience. The networking opportunities were unparalleled, and the knowledge gained has already made a positive impact on my career',
             'The event exceeded all my expectations. The lineup of speakers was impressive, and the atmosphere was filled with excitement and inspiration',
             'The event was a perfect blend of education and entertainment. I learned valuable insights while thoroughly enjoying myself',
             'What an incredible event! The energy in the room was electrifying, and I left with a renewed sense of purpose and determination',]},

    }
    selected_city = LSM_CITY_DETAIL.get(City_name)
    context = {'LSMcity': selected_city, 'City_name': City_name}
    return render(request, 'LSM_city_detail.html', context)


def city_faqs(request, city_name):
    context = {
        'city_name': city_name,
       
    }
    return render(request, 'FAQS.html', context)

# def city_sponsors(request, city_name):
#     context = {
#         'city_name': city_name,
#         # You can add more context variables if needed
#     }
#     return render(request, '#', context)

def city_sessions(request,city_name):
    context = {
         'city_name': city_name,
     }
    return render(request, 'Sessions.html', context)
def city_contact(request, city_name):
    context = {
         'city_name': city_name,
     }
    return render(request, 'Contact.html', context)
def city_speakers(request, city_name):
    context = {
         'city_name': city_name,
     }
    return render(request, 'Speakers.html', context)
def city_faqs(request, city_name):
    context = {
         'city_name': city_name,
    }
    return render(request, 'FAQS.html', context)
def city_sponsors(request, city_name):
    context = {
         'city_name': city_name,
    }
    return render(request, 'Sponsors.html', context)


def City_faqs(request, City_name):
    context = {
        'City_name': City_name,       
    }
    return render(request, 'LSM_FAQS.html', context)

# def city_sponsors(request, city_name):
#     context = {
#         'city_name': city_name,
#         # You can add more context variables if needed
#     }
#     return render(request, '#', context)

def City_sessions(request,City_name):
    context = {
         'City_name': City_name,
     }
    return render(request, 'LSM_Sessions.html', context)
def City_contact(request, City_name):
    context = {
         'city_name': City_name,
     }
    return render(request, 'LSM_Contact.html', context)
def City_speakers(request, City_name):
    context = {
         'City_name': City_name,
     }
    return render(request, 'LSM_Speakers.html', context)
def City_faqs(request, City_name):
    context = {
         'City_name': City_name,
    }
    return render(request, 'LSM_FAQS.html', context)
def City_sponsors(request, City_name):
    context = {
         'City_name': City_name,
    }
    return render(request, 'LSM_Sponsors.html', context)
def index(request):
    return render(request, "Map_index.html")

