import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# --------------------------------------------------------------
# Load data
# --------------------------------------------------------------
df = pd.read_pickle("../../data/interim/01_data_processed.pkl")

# --------------------------------------------------------------
# Plot single columns
# --------------------------------------------------------------
set_df = df[df["set"]==1]
plt.plot(set_df["acc_y"])

plt.plot(set_df["acc_y"].reset_index(drop=True))
# --------------------------------------------------------------
# Plot all exercises
# --------------------------------------------------------------
for label in df["label"].unique():
    subset = df[df["label"]==label]
    fig, ax = plt.subplots()
    plt.plot(subset[:100] ["acc_y"].reset_index(drop=True), label=label)
    plt.legend()
    plt.show()

# --------------------------------------------------------------
# Adjust plot settings
# --------------------------------------------------------------
mpl.style.use["seaborn-v0_8-deep"]
mpl.rcParams["figure.figsize"] = [20,5]
mpl.rcParams["figure.dpi"] = 100

# --------------------------------------------------------------
# Compare medium vs. heavy sets
# --------------------------------------------------------------
#comparing medium and heavy sets for squats. We can see that the heavy seta have higher acceleration in the y-axis.
category_df = df.query("label == 'squat'").query("participant == 'A'").reset_index()
fig, ax = plt.subplots()
category_df.groupby(["category"])["acc_y"].plot()
ax.set_ylabel("acc_y")
ax.set_xlabel("samples")
plt.legend()
# --------------------------------------------------------------
# Compare participants
# --------------------------------------------------------------
#so why we are using sort values here is because we want to plot it in order of the participant. If we don't sort it, the plot will be in random order. Reset index is used to reset the index to sample number, or else it will take time as the index which makes the plot look weird.
participant_df = df.query("label == 'bench'").sort_values("participant").reset_index()
fig, ax = plt.subplots()
participant_df.groupby(["participant"])["acc_y"].plot()  
ax.set_ylabel("acc_y")  
ax.set_xlabel("samples")
plt.legend()
# --------------------------------------------------------------
# Plot multiple axes
# --------------------------------------------------------------
label = "squat"
participant = "A"
all_axis_df = df.query("label == @label").query(f"participant == @participant").reset_index()
fig, ax = plt.subplots()
#we have to use two [[]] instead of [] because pandas does not allow us to plot a series with only one [].We want to plot the three axis in one plot.
all_axis_df[["acc_x", "acc_y", "acc_z"]].plot(ax=ax)
ax.set_ylabel("acc_y")
ax.set_xlabel("samples")
plt.legend()


# --------------------------------------------------------------
# Create a loop to plot all combinations per sensor
# --------------------------------------------------------------
labels = df["label"].unique()
participants = df["participant"].unique()
for label in labels:
    for participant in participants:
        all_axis_df = (
            df.query("label == @label").query(f"participant == @participant").reset_index()
        )
        #if length is > 0 for the df, then we plot it.
        if len(all_axis_df) > 0:
            fig, ax = plt.subplots()
            all_axis_df[["acc_x", "acc_y", "acc_z"]].plot(ax=ax)
            ax.set_ylabel("acc_y")
            ax.set_xlabel("samples")
            plt.title(f"{label} ({participant})".title())
            plt.legend()

for label in labels:
    for participant in participants:
        all_axis_df = (
            df.query("label == @label").query(f"participant == @participant").reset_index()
        )
        #if length is > 0 for the df, then we plot it.
        if len(all_axis_df) > 0:
            fig, ax = plt.subplots()
            all_axis_df[["gyr_x", "gyr_y", "gyr_z"]].plot(ax=ax)
            ax.set_ylabel("gyr_y")
            ax.set_xlabel("samples")
            plt.title(f"{label} ({participant})".title())
            plt.legend()

# --------------------------------------------------------------
# Combine plots in one figure
# --------------------------------------------------------------


# --------------------------------------------------------------
# Loop over all combinations and export for both sensors
# --------------------------------------------------------------