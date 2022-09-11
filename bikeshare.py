import time
import pandas as pd
import numpy as np

# city data which includes chicago, new york and washington
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # initializing city
    
    city = input('Please the city name these are options chicago, new york city or washington: ').lower()
    # validating the input by checking if it is within the given range
    while city.lower() not in ['chicago','new york city','washington']:
        print ('Sorry, that is not a correct option, try again.')
        city = input('Please the city name these are options chicago, new york city or washington: ').lower()    
        
    # TO DO: get user input for month (all, january, february, ... , june)
    
    # for ease of validation, all the correct inputs are inside the months list
    months = ['january', 'february', 'march', 'april', 'may', 
              'june', 'all']
    month = input('Please type the month for which you want the analysis, our database only has the first 6 months i.e. january, february, march, april, may or june. If you want all months type \'all\': ').lower()
    # validating the input by checking if it is in the months list
    while month.lower() not in months :
        print ('Sorry, that is not a correct option, try again.')
        month = input('Please type the month for which you want the analysis, our database only has the first 6 months i.e. january, february, march, april, may or june. If you want all months type \'all\': ').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # for ease of validation, all the correct inputs are inside the days list

    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 
              'friday', 'saturday', 'all']
    day = input('Please type the day for which you want the analysis e.g. sunday, monday and so on. If you want all days type \'all\': ').lower()
    # validaing the input checking if it is inside the days list
    while day not in days :
        print ('Sorry, that is not a correct option, try again.')
        day = input('Please type the day for which you want the analysis e.g. sunday, monday and so on. If you want all days type \'all\': ').lower()
    
    
    print (city, month, day)
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """    
    # loading the csv file based on the city selected
    df = pd.read_csv(CITY_DATA[city])
    # convert Start Time columnt to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extracting the month and day 
    # this code was taken from the practice solution #3
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    # if not all days was selected filter the data
    if day != 'all':
        print(day)
       # filter based on the day of the week
        df = df[df['day'] == day.capitalize()]
    # if not all months was selected filter the data
    if month != 'all': 
        months = ['january', 'february', 'march', 'april', 'may', 'june']
       # filtering the data based on the selected month
        print(month, months.index(month)+1)
        df = df[df['month'] == months.index(month)+1]
    return df 


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print (df['month'].mode())
    # TO DO: display the most common month
    print('\nThe most common month is: ', df['month'].mode()[0], '\n')

    # TO DO: display the most common day of week

    print('\nThe most common day of the week is: ', df['day'].mode()[0], '\n')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('\nThe most common month start hour is: ', df['hour'].mode()[0], '\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nThe most commonly used start station is: ', df['Start Station'].mode()[0], '\n')
    # TO DO: display most commonly used end station
    print('\nThe most commonly used end station is: ', df['End Station'].mode()[0], '\n')

    # TO DO: display most frequent combination of start station and end station trip

    frequent = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False).index
    print('The most frequent combination of start station and end station trip is start station: ',frequent[0][0], ', and end station: ', frequent[0][1], '\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    print('\nThe total travel time is: ', df['Trip Duration'].sum())
    # TO DO: display mean travel time
    print('\nThe mean travel time is: ', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nThe counts of user types are:\n', df['User Type'].value_counts().to_string())
    # TO DO: Display counts of gender
    # washington dataset doesnt include the gender column that's why we are checking its presence here

    if 'Gender' in df.columns: 
        print('\nThe counts of genders are:\n', df['Gender'].value_counts().to_string())
    
    # TO DO: Display earliest, most recent, and most common year of birth
    # washington dataset doesnt include the birth year column that's why we are checking its presence here
    if 'Birth Year' in df.columns: 
        print('\nThe earliest year of birth is: ', df['Birth Year'].min())
        print('\nThe most recent year of birth is: ', df['Birth Year'].max())
        print('\nThe most common year of birth is: ', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    raw_data = input('\nWould like to see some of the raw data? Enter yes or no: ')
    no_of_rows = 0
    while raw_data.lower() == 'yes': 
        print (df.iloc[no_of_rows:no_of_rows+5])
        no_of_rows+=5
        raw_data = input('\nWould like to see some more raw data? Enter yes or no: ')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        # used to display raw data
        display_raw_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
