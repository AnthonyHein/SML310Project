This directory contains the most important data files for this analysis.

`X_[train/dev/test]_preprocess_without_race.csv`: Contains the input used for training/validating/testing models.

- `horse[1/2]_age` - The age of horse 1/2 in years at the start of the race.
- `horse[1/2]_saddle` - The saddle number of horse 1/2.
- `horse[1/2]_decimalPrice` - The \textit{reciprocal} of the decimal odds for horse 1/2 (larger means more favored to win).
- `horse[1/2]_isFav` - Boolean whether horse 1/2 has the (weakly) largest decimal odds of all horses in the race.
- `horse[1/2]_outHandicap` - Amount of additional weight (possibly zero) placed on horse 1/2.
- `horse[1/2]_RPR` - Rating by racecourse officials of horse 1/2, similar to the odds except not determined by the public.
- `horse[1/2]_weight` - Weight of the horse 1/2 (in kilograms).
- `horse[1/2]_d_last_race` - Number of days since horse 1/2's jockey's last race.
- `horse[1/2]_d_first_race` - Number of days since horse 1/2's jockey's first race.
- `horse[1/2]_prev_[1/2/3]_position` - Finishing position of horse 1/2's jockey in their 1st/2nd/3rd most previous race.
- `horse[1/2]_prev_[1/2/3]_finishing_time_ratio` - Finishing time ratio of horse 1/2's jockey in their 1st/2nd/3rd most previous race.
- `horse[1/2]_prev_[1/2/3]_global_finishing_time_ratio` - Global finishing time ratio of horse 1/2's jockey in their 1st/2nd/3rd most previous race.
- `horse[1/2]_prev_[1/2/3]_[position/finishing_time_ratio]_course` - Finishing position/ finishing time ratio of horse 1/2's jockey in their 1st/2nd/3rd most previous race on the same course.
- `horse[1/2]_prev_[1/2/3]_[position/finishing_time_ratio]_metric` - Finishing position/ finishing time ratio of horse 1/2's jockey in their 1st/2nd/3rd most previous race on the same distance.
- `horse[1/2]_prev_[1/2/3]_[position/finishing_time_ratio]_ncond` - Finishing position/ finishing time ratio of horse 1/2's jockey in their 1st/2nd/3rd most previous race on the same track condition.
- `horse[1/2]_prev_[1/2/3]_[position/finishing_time_ratio]_runners` - Finishing position/ finishing time ratio of horse 1/2's jockey in their 1st/2nd/3rd most previous race with the same number of runners.
- `horse[1/2]_prev_[1/2/3]_[position/finishing_time_ratio]_month` - Finishing position/ finishing time ratio of horse 1/2's jockey in their 1st/2nd/3rd most previous race in the same month.
- `horse[1/2]_prev_[1/2/3]_[position/finishing_time_ratio]_temp` - Finishing position/ finishing time ratio of horse 1/2's jockey in their 1st/2nd/3rd most previous race in a similar temperature.
- `horse[1/2]_prev_[1/2/3]_[position/finishing_time_ratio]_msl` - Finishing position/ finishing time ratio of horse 1/2's jockey in their 1st/2nd/3rd most previous race in a similar barometric pressure.
- `horse[1/2]_prev_[1/2/3]_[position/finishing_time_ratio]_rain` - Finishing position/ finishing time ratio of horse 1/2's jockey in their 1st/2nd/3rd most previous race in a similar rainfall.
- `horse[1/2]_prev_[1/2/3]_[position/finishing_time_ratio]_rhum` - Finishing position/ finishing time ratio of horse 1/2's jockey in their 1st/2nd/3rd most previous race in a similar humidity.

---

`X_[train/dev/test]_pairwise_winner_labels.csv`: Contains the targets for the above file. 1 if horse 1 finished earlier than horse 2 and 0 otherwise.

---

`races_selected_trimmed_clean.csv`: A dataset of over 20,000 races from Ireland between 1990 and 2020 that is novel in its incorporation of weather readings.

- `rid` - Race ID.
- `course` - Racecourse the race was run on.
- `title` - Title of the race (unused).
- `winningTime` - Finishing time of the first place finisher.
- `metric` - The distance (m) the race was run over.
- `ncond` - The track condition code.
- `class` - The class of the race (unused).
- `runners` - The number of runners in the race.
- `margin` - The sum of the reciprocal demical odds across all runners in the race (unused).
- `1st_place_rank_in_odds` - The first place finisher's rank in the public odds.
- `2nd_place_rank_in_odds` - The second place finisher's rank in the public odds.
- `3rd_place_rank_in_odds` - The third place finisher's rank in the public odds.
- `1st_rank_in_odds_place` - The finishing position of the horse ranked first in the public odds.
- `2nd_rank_in_odds_place` - The finishing position of the horse ranked second in the public odds.
- `3rd_rank_in_odds_place` - The finishing position of the horse ranked third in the public odds.
- `placeAvailable` - Whether the place bet is available for this race.
- `showAvailable` - Whether the show bet is available for this race.
- `favoriteWon` - Whether the horse ranked first in the public odds won.
- `favoritePlaced` - Whether the horse ranked first in the public odds placed.
- `favoriteShowed` - Whether the horse ranked first in the public odds showed.
- `lat` - The latitude of the racecourse this race was run on.
- `lng` - The longitude of the racecourse this race was run on.
- `datetime` - The datetime this race was run at.
- `station no` - The number of the Met Eireann station from which weather was used.
- `station name` - The name of the Met Eireann station from which weather was used.
- `station lat` - The latitutde of the Met Eireann station from which weather was used.
- `station lng` - The longitude of the Met Eireann station from which weather was used.
- `dist to station` - The distance from the racecourse to the Met Eireann station from which weather was used.
- `station reading date` - The datetime of the weather reading that was used.
- `temp` - The temperature of the weather reading (C).
- `msl` - The mean sea level pressure of the weather reading (hPa).
- `rain` - The rainfall of the weather reading (mm).
- `rhum` - The relative humidity of the weather reading (%).
- `station reading timedelta` - The difference in time between the race start and weather reading.

---

`horses_selection_trimmed_clean_augmented.csv`: Data on each horse in each race which occurs in the `races_selected_trimmed_clean.csv` dataset.

- `rid` - Race ID.
- `horseName` - Horse name.
- `age` - Age of the horse in years.
- `saddle` - Saddle number of the horse.
- `decimalPrice` - Reciprocal decimal odds of the horse.
- `isFav` - Whether the horse is projected to win by the public odds.
- `trainerName` - Trainer of the horse.
- `jockeyName` - Jockey of the horse.
- `position` - Finishing position of the horse.
- `positionL` - The lengths this horse finished behind its predecessor.
- `dist` - The lengths this horse finished behind the race winner.
- `outHandicap` - The handicap of the horse.
- `RPR` - The racing post rating of the horse.
- `TR` - The topspeed rating of the horse (unused).
- `OR` - The official rating of the horse (unused).
- `father` - The horse's father (unused).
- `mother` - The horse's mother (unused).
- `gfather` - The horse's grandfather. (unused)
- `weight` - The weight of the horse.
- `res_win` - Whether this horse won the race (unused).
- `res_place` - Whether this horse placed in the race (unused).
- `res_show` -  Whether this horse showed in the race (unused).
- `finishing time` - The (estimated) finishing time of the horse.
- `finishing time ratio` - The (estimated) finishing time ratio of the horse.
