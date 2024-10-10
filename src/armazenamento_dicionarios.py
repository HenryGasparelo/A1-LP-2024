"""MODULO DE ARMAZENAMENTO DE DICIONARIOS PARA AS FUNCOES"""

dicionario_Student = {
    'No': 0,
    'Yes, part-time': 1,
    'Yes, full-time': 2
}

dicionario_Employment = {
    'Employed part-time': 1,
    'Independent contractor, freelancer, or self-employed': 1,
    'Employed full-time': 2,
    "Not employed, and not looking for work": 0,
    "Not employed, but looking for work": 0,
    "Retired": 0
}

dicionario_FormalEducation_hipotese4 = {
    'Some college/university study without earning a degree': 'Nao possui ensino superior',
    'Associate degree': 'Possui ensino superior',
    'Bachelor’s degree (BA, BS, B.Eng., etc.)': 'Possui ensino superior',
    'Master’s degree (MA, MS, M.Eng., MBA, etc.)': 'Possui ensino superior',
    'Professional degree (JD, MD, etc.)': 'Possui ensino superior',
    'Other doctoral degree (Ph.D, Ed.D., etc.)': 'Possui ensino superior',
    "I never completed any formal education": 'Nao possui ensino superior',
    "Primary/elementary school": 'Nao possui ensino superior',
    "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)": 'Nao possui ensino superior'
}

dicionario_FormalEducation_hipotese3 = {
    'Some college/university study without earning a degree': 'Sem educacao formal',
    'Associate degree': 'Educacao basica',
    'Bachelor’s degree (BA, BS, B.Eng., etc.)': 'Graduacao',
    'Master’s degree (MA, MS, M.Eng., MBA, etc.)': 'Mestrado',
    'Professional degree (JD, MD, etc.)': 'Doutorado profissional',
    'Other doctoral degree (Ph.D, Ed.D., etc.)': 'Doutorado',
    "I never completed any formal education": 'Sem educacao formal',
    "Primary/elementary school": 'Educacao basica',
    "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)": 'Educacao basica'
}

dicionario_YearsCoding = {
    '0-2 years': 1,
    '3-5 years': 4,
    '6-8 years': 7,
    '9-11 years': 10,
    '12-14 years': 13,
    '15-17 years': 16,
    '18-20 years': 19,
    '21-23 years': 22,
    '24-26 years': 25,
    '27-29 years': 28,
    '30 or more years': 30
}

dicionario_JobSatisfaction = {
    'Extremely dissatisfied': 0,
    'Moderately dissatisfied': 1,
    'Slightly dissatisfied': 2,
    'Neither satisfied nor dissatisfied': 3,
    'Slightly satisfied': 4,
    'Moderately satisfied': 5,
    'Extremely satisfied': 6
}

dicionario_CareerSatisfaction = {
    'Extremely dissatisfied': "Baixo",
    'Moderately dissatisfied': "Baixo",
    'Slightly dissatisfied': "Medio",
    'Neither satisfied nor dissatisfied': "Medio",
    'Slightly satisfied': "Medio",
    'Moderately satisfied': "Alto",
    'Extremely satisfied': "Alto"
}

dicionario_JobSearchStatus = {
    'I am not interested in new job opportunities': 0,
    'I’m not actively looking, but I am open to new opportunities': 1,
    'I am actively looking for a job': 2
}

dicionario_LastNewJob = {
    "I've never had a job": 0,
    'Less than a year ago': 1,
    'Between 1 and 2 years ago': 1.5,
    'Between 2 and 4 years ago': 3,
    'More than 4 years ago': 4
}

dicionario_UpdateCV = {
    'I had a negative experience or interaction at work': 1,
    'I received negative feedback on my job performance': 1,
    'I received bad news about the future of my company or department': 1,
    'My job status or other personal status changed': 2,
    'I did not receive an expected change in compensation': 2,
    'A friend told me about a job opportunity': 3,
    'A recruiter contacted me': 3,
    'I saw an employer’s advertisement': 3
}

dicionario_HoursComputer = {
    'Less than 1 hour': 10,
    '1 - 4 hours': 10,
    '5 - 8 hours': 8,
    '9 - 12 hours': 6,
    'Over 12 hours': 4
}

dicionario_HoursOutside = {
    'Less than 30 minutes': 1,
    '30 - 59 minutes': 3,
    '1 - 2 hours': 6,
    '3 - 4 hours': 8,
    'Over 4 hours': 10
}

dicionario_SkipMeals = {
    'Never': 10,
    '1 - 2 times per week': 6,
    '3 - 4 times per week': 3,
    'Daily or almost every day': 1
}

dicionario_Exercise = {
    "I don't typically exercise": 0,
    '1 - 2 times per week': 4,
    '3 - 4 times per week': 8,
    'Daily or almost every day': 10
}

dicionario_Age = {
    'Under 18 years old': 18,
    '18 - 24 years old': 21,
    '25 - 34 years old': 29.5,
    '35 - 44 years old': 39.5,
    '45 - 54 years old': 49.5,
    '55 - 64 years old': 59.5,
    '65 years or older': 65
}
