import pandas as pd
import plotly.graph_objs as go
import ekkono.primer as primer


def rearrange_df(df: pd.DataFrame):
    dicts = {}
    for variable in df.columns:
        if variable != "id":
            df_column = pd.DataFrame()
            for index, row in df.iterrows():
                df_column.loc[index, variable + "_" + str(int(row["id"]))] = row[
                    variable
                ]
            dicts[variable] = df_column
    df_new = pd.concat(dicts.values(), axis="columns")
    return df_new


def time_parse(df_new: pd.DataFrame, data_directory: str):
    collection_day = day_finder(data_directory)
    index = collection_day + "0" + df_new.index.astype(str)
    time_index = [pd.to_datetime(i, format="%Y%m%d%H%M%S") for i in index]
    df_new.set_index(pd.Index(time_index), inplace=True)
    return df_new


def day_finder(data_directory: str):
    start = data_directory.find("ARN-") + len("ARN-")
    end = data_directory.find("/", start)
    collection_day = data_directory[start:end]
    return collection_day


def event_parser():
    """NOT USED ANYMORE parsing event info function"""

    data = """
    // menzies

    064712 inside  (enter)
    064812 outside (leave)
    064901 inside  (enter)
    064955 outside (leave)
    065034 inside  (enter)
    065128 outside (leave)

    // terminal 3

    065207 inside  (enter)
    065336 outside (leave)
    065420 inside  (enter)
    065454 outside (leave)
    065518 inside  (enter)
    065552 outside (leave)

    // terminal 5

    065738 inside  (enter)
    065904 outside (leave)
    065944 inside  (enter)
    070112 outside (leave)
    070157 inside  (enter)
    070325 outside (leave)

    // CB

    070406 inside (soft-enter)
    070418 inside  (enter)
    070611 outside (leave)
    070713 inside (soft-enter)
    070722 inside  (enter)
    070916 outside (leave)
    071027 inside (soft-enter)
    071037 inside  (enter)
    071229 outside (leave)
    """

    # Split the data into blocks using "//"
    blocks = [block.strip() for block in data.strip().split("//") if block.strip()]

    # Initialize an empty dictionary
    log_dict = {}

    # Iterate over each block
    for block in blocks:
        lines = block.split("\n")
        tag_info = lines[0].strip()
        tag_info = tag_info.replace("\n", " ")
        for line in lines[1:]:
            parts = line.split()
            if len(parts) >= 3:
                time = parts[0][1:]
                tag = parts[-1][1:-1]
                log_dict[time] = tag + " (" + tag_info + ")"

    return log_dict


def event_parser_times(data_directory: str):
    """parsing event info function"""

    collection_day = day_finder(data_directory)

    data = """
    // menzies

    064712 inside  (enter)
    064812 outside (leave)
    064901 inside  (enter)
    064955 outside (leave)
    065034 inside  (enter)
    065128 outside (leave)

    // terminal 3

    065207 inside  (enter)
    065336 outside (leave)
    065420 inside  (enter)
    065454 outside (leave)
    065518 inside  (enter)
    065552 outside (leave)

    // terminal 5

    065738 inside  (enter)
    065904 outside (leave)
    065944 inside  (enter)
    070112 outside (leave)
    070157 inside  (enter)
    070325 outside (leave)

    // CB

    070406 inside (soft-enter)
    070418 inside  (enter)
    070611 outside (leave)
    070713 inside (soft-enter)
    070722 inside  (enter)
    070916 outside (leave)
    071027 inside (soft-enter)
    071037 inside  (enter)
    071229 outside (leave)
    """

    # Split the data into blocks using "//"
    blocks = [block.strip() for block in data.strip().split("//") if block.strip()]

    # Initialize an empty dictionary
    log_dict = {}

    # Iterate over each block
    for block in blocks:
        lines = block.split("\n")
        tag_info = lines[0].strip()
        tag_info = tag_info.replace("\n", " ")
        for line in lines[1:]:
            parts = line.split()
            if len(parts) >= 3:
                time = (
                    collection_day + parts[0][1:]
                )  # first term of summation is the collection day
                time = pd.to_datetime(time, format="%Y%m%d%H%M%S%f")
                tag = parts[-1][1:-1]
                log_dict[time] = tag + " (" + tag_info + ")"

    log_dict = {
        k: v for k, v in log_dict.items() if "soft" not in v
    }  # filter out soft-enter events

    return log_dict


def keep_one_signal(variable_to_keep: str, df_new: pd.DataFrame):
    drop_variables = []
    for i in df_new.columns:
        if variable_to_keep not in i:
            drop_variables.append(i)
    df_snr = df_new.drop(columns=drop_variables)
    return df_snr


def plotly_df(df_plot, html_name: str, index_tags: dict):
    fig = go.Figure()

    if isinstance(df_plot, pd.Series):
        df_plot = df_plot.to_frame()

    for col in df_plot.columns:
        fig.add_trace(
            go.Scatter(x=df_plot.index, y=df_plot[col], mode="lines", name=col)
        )

    for index, tag in index_tags.items():
        fig.add_vline(x=index, line_dash="dot", line_color="rgba(0, 0, 9, 0.5)")
        fig.add_annotation(
            x=index,
            y=15,
            text=tag,
            showarrow=True,
            arrowhead=1,
            xshift=-5,
            yshift=150,
            textangle=50,
            font=dict(size=10),
        )

    fig.update_layout(title="Signals per satellite")
    fig.show()

    fig.write_html(html_name)


def plotly_df2(df1, df2, html_name: str, index_tags: dict):
    fig = go.Figure()

    if isinstance(df1, pd.Series):
        df1 = df1.to_frame()
    if isinstance(df2, pd.Series):
        df2 = df2.to_frame()

    for col in df1.columns:
        fig.add_trace(go.Scatter(x=df1.index, y=df1[col], mode="lines", name=col))

    for col in df2.columns:
        fig.add_trace(
            go.Scatter(x=df2.index, y=df2[col], mode="lines", name=col, yaxis="y2")
        )

    for index, tag in index_tags.items():
        fig.add_vline(x=index, line_dash="dot", line_color="rgba(0, 0, 9, 0.5)")
        fig.add_annotation(
            x=index,
            y=15,
            text=tag,
            showarrow=True,
            arrowhead=1,
            xshift=-5,
            yshift=150,
            textangle=50,
            font=dict(size=10),
        )

    fig.update_layout(
        title="Selected signals",
        yaxis=dict(title="Primary Y-axis"),
        yaxis2=dict(title="Secondary Y-axis", overlaying="y", side="right"),
    )

    fig.show()
    fig.write_html(html_name)


def pandas_to_primer(data):
    attributes = []
    for col in data.columns:
        attributes.append(primer.AttributeMeta(str(col)))
    dataset = primer.Dataset(attributes)
    for idx, row in data.iterrows():
        dataset.create_instance(row.tolist())
    return dataset


def create_line_plot(data_dict, title_plot, colors=["red", "green", "blue"]):
    fig = go.Figure()

    for i, (name, data) in enumerate(data_dict.items()):
        color = colors[i] if colors and i < len(colors) else None
        fig.add_trace(
            go.Scatter(
                x=list(range(len(data))),
                y=data,
                mode="lines",
                name=name,
                line=dict(color=color) if color else {},
            )
        )

    fig.update_layout(title=title_plot, xaxis_title="Index", yaxis_title="Value")

    fig.show()
    html_name = "../../figures/" + title_plot + ".html"
    fig.write_html(html_name)


def add_column_location(df_snr: pd.DataFrame, index_tags_times: dict):
    """Add location as a column based on the entering exiting events"""
    df_snr.loc[:, "location"] = 0
    for n, timestamps in enumerate(index_tags_times.keys()):
        if n % 2 == 0:
            df_snr.loc[
                list(index_tags_times.keys())[n] : list(index_tags_times.keys())[n + 1],
                "location",
            ] = 1
    return df_snr


class PipelineCreator:
    def __init__(self, df_snr: pd.DataFrame, target: str = "location"):
        self.df_snr = df_snr
        self.target = target

    def add_deltas(self, windows: list):
        """Add as columns two deltas to df; one for entering (negative slope),
        one for exiting (positive slope)"""
        df_snr_diff = pd.DataFrame(index=self.df_snr.index)
        df_snr_dropped = self.df_snr.drop(columns=[self.target])
        for window in windows:
            diff_sum = df_snr_dropped.diff(periods=window).sum(axis="columns")
            column_name = f"delta{window}"
            df_snr_diff[column_name] = diff_sum
            df_snr_diff[column_name + "_in"] = df_snr_diff[column_name].where(
                df_snr_diff[column_name] < 0, 0
            )
            df_snr_diff[column_name + "_out"] = df_snr_diff[column_name].where(
                df_snr_diff[column_name] > 0, 0
            )
            df_snr_diff.drop(columns=[column_name], inplace=True)
        return df_snr_diff

    def add_mins(self, windows: list):
        """ "Add as column the min value of a rolling window"""
        mins = pd.DataFrame(index=self.df_snr.index)
        df_snr_dropped = self.df_snr.drop(columns=[self.target])
        for window in windows:
            min_values = df_snr_dropped.rolling(window=window).min().max(axis="columns")
            column_name = f"min_max{window}"
            mins[column_name] = min_values
        return mins


def anomaly_detector(
    df: pd.DataFrame,
    n_points_calibration: float,
    nbr_of_points: float,
    sensitivity: float,
    target: str,
    df_snr: pd.DataFrame,
):
    """Convert to primer dataset and create Anomaly detector"""
    ds_selected_signals = pandas_to_primer(df)
    split = primer.InstancePartitioner(
        ds_selected_signals, n_points_calibration / ds_selected_signals.instance_count
    )
    ds_train, ds_test = split[0], split[1]
    shift = ds_train.instance_count
    targets = df.columns.to_list()
    anomaly_scores = {}
    for variable in targets:
        templ = ds_selected_signals.pipeline_template
        for col in ds_selected_signals.attributes:
            if str(col) != variable:
                templ.filter_attribute(str(col))
        anomaly_detector_diff = primer.ModelFactory.create_anomaly_detector(
            templ, nbr_of_points=nbr_of_points, sensitivity=sensitivity
        )
        primer.ModelTrainer.calibrate(anomaly_detector_diff, ds_train)
        anomaly_scores["Anomaly score " + variable] = []
        for i, instance in enumerate(ds_test):
            score = anomaly_detector_diff.score(instance)
            anomaly_scores["Anomaly score " + variable].append(score)
    anomaly_scores[target] = df_snr.iloc[shift:, :][target]
    # anomaly_scores[target] = df_snr[target]
    print(f'RAM memory usage (excluding pipeline): {anomaly_detector_diff.memory_usage/1000}' ' kB')
    return anomaly_scores, targets
