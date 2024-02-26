// src/services/sportsFacilityService.js

const BASE_URL = '/api/sport-facilities';

const getAllFacilities = async () => {
  const response = await fetch(BASE_URL);
  if (!response.ok) {
    throw new Error('Failed to fetch facilities');
  }
  return response.json();
};

const getFacilityById = async (facilityId) => {
  const response = await fetch(`${BASE_URL}/${facilityId}`);
  if (!response.ok) {
    throw new Error('Failed to fetch facility details');
  }
  return response.json();
};

const createFacility = async (facilityData) => {
  const response = await fetch(BASE_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(facilityData),
  });
  if (!response.ok) {
    throw new Error('Failed to create facility');
  }
  return response.json();
};

const updateFacility = async (facilityId, facilityData) => {
  const response = await fetch(`${BASE_URL}/${facilityId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(facilityData),
  });
  if (!response.ok) {
    throw new Error('Failed to update facility');
  }
  return response.json();
};

const deleteFacility = async (facilityId) => {
  const response = await fetch(`${BASE_URL}/${facilityId}`, {
    method: 'DELETE',
  });
  if (!response.ok) {
    throw new Error('Failed to delete facility');
  }
};

const SportsFacilityService = {
  getAllFacilities,
  getFacilityById,
  createFacility,
  updateFacility,
  deleteFacility,
};

export default SportsFacilityService;
