import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    print('You can select data on Chicago, New York or Washington.')

    # Ask for city and check for correct city names

    while True:
        city = input('\nPlease enter a city name: ').lower()
        if city in ['chicago', 'new york', 'washington']:
            break
        else:
            print("\nSorry, this analysis is limited to Chicago, New York and Washington. Please pick one of those cities")

    # Ask for month and check for correct input
    print('\nThanks, now select a month.')

    while True:
        month = input('\nPlease enter a month (January to June, you may also select \'all\' months): ').lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("\nSorry, this analysis is limited to the month January until June. Please pick one month or \'all\'")


    # Ask for month and check for correct input

    print('\nThanks, and now select a day.')

    while True:
        day = input('\nPlease enter a day of the week, you may also select \'all\' days: ').lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("\nSorry, this is not a day of the week. Please pick one day or \'all\'")


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month =  months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['weekday'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()
    print('Most common month:', most_common_month)

    # display the most common day of week
    most_common_dow = df['weekday'].mode()
    print('Most common DOW:', most_common_dow)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()
    print('Most common starting hour:', most_common_hour)

    print("\nThis took %s seconds." % round((time.time() - start_time), 3))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start = df['Start Station'].mode()
    print('Most commonly used starting station:', most_common_start)

    # display most commonly used end station
    most_common_end = df['End Station'].mode()
    print('Most commonly used ending station:', most_common_end)

    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_trip = df['trip'].mode()
    print('Most commonly taken trip:', most_common_trip)

    print("\nThis took %s seconds." % round((time.time() - start_time), 3))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time in seconds:', total_travel_time)

    # display mean travel time
    mean_travel_time = round((df['Trip Duration'].mean()), 3)
    print('Mean travel time in seconds:', mean_travel_time)

    print("\nThis took %s seconds." % round((time.time() - start_time), 3))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    user_gender = df['Gender'].value_counts()
    print(user_gender)

    # Display earliest, most recent, and most common year of birth
    user_min_birthyear = df['Birth Year'].min()
    user_max_birthyear = df['Birth Year'].max()
    user_mode_birthyear = df['Birth Year'].mode()
    print('\nEarliest year of birth:', user_min_birthyear)
    print('\nMost recent year of birth: ', user_max_birthyear)
    print('\nMost common year of birth: ', user_mode_birthyear)

    print("\nThis took %s seconds." % round((time.time() - start_time), 3))
    print('-'*40)


def show_detail_data(df):
    """Displays the detailled data on selected city, month and day."""

    for i in range(0, len(df), 5):
        detail_data = input('\nWould you like to see more detailled data of this analysis? (yes/no) ').lower()
        if detail_data == 'yes':
            print(df.iloc[i:i+5])
        if detail_data == 'no':
            print('Ok, leaving the detailled data display.')
            break
        if detail_data != 'yes' and detail_data != 'no':
            print("\nPlease type \'yes\' or \'no\'")

def restart():
        restart = input('\nWould you like to restart? (yes/no): ').lower()
        if restart == 'yes':
            main()
        if restart == 'no':
            print('Ok, leaving the analysis program.\n')
        if restart != 'yes' and restart != 'no':
            print("\nPlease type \'yes\' or \'no\'")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)

        if city in ['chicago', 'new york']:
            user_stats(df)
        else:
            print("\nNo user specific data available for Washington")

        show_detail_data(df)
        restart()
        break


if __name__ == "__main__":
	main()
