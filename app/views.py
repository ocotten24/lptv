from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render
from dataclasses import dataclass

@dataclass
class Team:
    teamName: str
    description: str
    teamMembers: list[str]


def all_teams_view(request: HttpRequest) -> HttpResponse:
    context = {
        'teams':[
        Team(
            'Management',
            'The Management Team plays a crucial role in ensuring the smooth operation of Basecamp Coding Academy. Their primary responsibilities include creating and updating chore schedules for the program, ensuring that students have assigned tasks and responsibilities. Additionally, they oversee the management of supplies and equipment, making sure that everything needed for daily activities is available.',
            ['Owen','Jeremiah','Nick','Ab','Abigail','Mathew'] ),

        Team(
            'Community',
            'The Community Team is dedicated to fostering a sense of togetherness and engagement within Basecamp Coding Academy. They are responsible for organizing various events and activities that bring students and staff together. These events can range from social gatherings to bowling, all aimed at building a strong and supportive community within the program.',
            ['Jordan','Joby','Aj','Micah','Caleb'] ),

        Team(
            'Documentation',
            "The Documentation Team is responsible for capturing and sharing the experiences and activities at Basecamp Coding Academy. They actively manage the program's social media presence and post pictures and videos that they take. Their role involves creating a visual record of the program's journey, sharing updates, and providing an insight into life at Basecamp Coding Academy through various social media platforms.",
            ['Conner','Kaleigh','Blair','Mina','Jay','Joshua','Kayleah',] ),

        Team(
            'Procurement',
            'The Procurement Team focuses on the logistics of sustenance by handling the acquisition of food supplies for the program. They are responsible for purchasing the necessary ingredients and supplies to provide meals for students and staff. In addition to sourcing food, they also play a role in meal preparation, ensuring everyone is well-fed.',
            ['Adrian','Bryce','Big John','Blaine','Wyatt'] )
        ]}
    return render(request, "index.html", context)

def team_detail_view(request: HttpRequest, name: str) -> HttpResponse:
    team_info = None

    if name == 'Management':
        team_info = Team(
            'Management',
            'The Management Team plays a crucial role in ensuring the smooth operation of Basecamp Coding Academy. Their primary responsibilities include creating and updating chore schedules for the program, ensuring that students have assigned tasks and responsibilities. Additionally, they oversee the management of supplies and equipment, making sure that everything needed for daily activities is available.',
            ['Owen', 'Jeremiah', 'Nick', 'Ab', 'Abigail', 'Matthew']
        )
    elif name == 'Community':
        team_info = Team(
            'Community',
            'The Community Team is dedicated to fostering a sense of togetherness and engagement within Basecamp Coding Academy. They are responsible for organizing various events and activities that bring students and staff together. These events can range from social gatherings to bowling, all aimed at building a strong and supportive community within the program.',
            ['Jordan', 'Joby', 'Aj', 'Micah', 'Caleb']
        )
    elif name == 'Documentation':
        team_info = Team(
            'Documentation',
            "The Documentation Team is responsible for capturing and sharing the experiences and activities at Basecamp Coding Academy. They actively manage the program's social media presence and post pictures and videos that they take. Their role involves creating a visual record of the program's journey, sharing updates, and providing an insight into life at Basecamp Coding Academy through various social media platforms.",
            ['Conner', 'Kaleigh', 'Blair', 'Mina', 'Jay', 'Joshua', 'Kayleah']
        )
    elif name == 'Procurement':
        team_info = Team(
            'Procurement',
            'The Procurement Team focuses on the logistics of sustenance by handling the acquisition of food supplies for the program. They are responsible for purchasing the necessary ingredients and supplies to provide meals for students and staff. In addition to sourcing food, they also play a role in meal preparation, ensuring everyone is well-fed.',
            ['Adrian', 'Bryce', 'Big John', 'Blaine', 'Wyatt']
        )

    

    context = {'team': team_info}
    return render(request, "teamDetails.html", context)
