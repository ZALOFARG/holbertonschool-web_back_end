import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const item1 = new ClassRoom(19);
  const item2 = new ClassRoom(20);
  const item3 = new ClassRoom(34);

  return [
    item1,
    item2,
    item3,
  ];
}
