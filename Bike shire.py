import time
import pandas as pd
import numpy as np

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
    cities=["chicago","new york city","washington"]
    city = input("\nEnter a city from those cities(chicago, new york city, washington): ").lower()
    while str(city) not in cities:
        print("enter a valid option")
        city = input("\nEnter a city from those cities(chicago, new york city, washington): ").lower()
       
    
   
    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("\nEnter a specific month from (january, february, ... , june) or enter all : ").lower() 
    monthss=["january","februaury","march","april","may","june","all"]
    while month not in monthss:
        print("enter a valid option")
        month=input("\nEnter a specific month from (january, february, ... , june) or enter all : ") .lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=["saturday","sunday","monday","tuesday","wednesday","thursday","friday","all"]
    day=input ("\nEnter a specific day from a week or enter all: ").lower()
    while day not in days:
        print("enter a valid option")
        day=input ("\nEnter a specific day from a week or enter all: ").lower()
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]
    print("\nthe most common month is {}".format(popular_month))
    # TO DO: display the most common day of week
    popular_day=df['day_of_week'].mode()[0]
    print("\nthe most common day is {}".format(popular_day))
    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print("\nthe most common start hour is {}".format(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("\nThe total time travel time is {}.".format(total_travel_time))
          

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print("\nThe mean time travel is {}.".format(mean_travel_time))      

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    
    print("\ncounts of user types are {}.".format(user_types))
          # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts=df['Gender'].value_counts()
        print("\ncounts of gender are {}.".format(gender_counts))      

    # TO DO: Display earliest, most recent, and most common year of birth
        The_most_common_year=df['Birth Year'].mode()[0]
        The_earliest_year=df['Birth Year'].max()
        The_most_recent_year=df['Birth Year'].min()
        print("\nThe most common yeat of birth is {}.".format(The_most_common_year))
        print("\nThe earlist year is {}.".format(The_earliest_year))
        print("\nThe most recent year is {}.".format(The_most_recent_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most frequent stations of travel."""
    print('\nCalculating The Most Frequent stations of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common Start Station
    popular_start_station=df['Start Station'].mode()[0]
    print("\nthe most common start station is {}".format(popular_start_station))
    # TO DO: display the most common End Station
    popular_end_station=df['End Station'].mode()[0]
    print("\nthe most common end station is {}".format(popular_end_station))
    # TO DO: display the most common route
    df['route']=df['Start Station']+","+df['End Station']
    popular_route=df['route'].mode()[0]
    print("\nthe most common route is {}".format(popular_route))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw_Data(df):
    raw = input('\nWould you like to see raw data? Enter yes or no.\n')
    num=5
    while raw.lower() == "yes":
        print(df.head(num))
        raw = input('\nWould you like to see more raw data? Enter yes or no.\n')
        num+=5
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_Data(df)
        time_stats(df)         
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
