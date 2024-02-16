import re

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    data = data[(data['passenger_count']>0) & (data['trip_distance']>0)]
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    
    def camel_to_snake(name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    # Rename columns using the camel_to_snake function
    data.columns = [camel_to_snake(col) for col in data.columns]

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert ('vendor_id' in output.columns.tolist()), 'there in no vendor_id column'
    assert (output['passenger_count'].isin([0]).sum() == 0), 'passenger_count is greater than 0'
    assert (output['trip_distance'].isin([0]).sum() == 0), 'trip_distance is greater than 0'
