import { TestBed } from '@angular/core/testing';

import { MybookService } from './mybook.service';

describe('MybookService', () => {
  let service: MybookService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MybookService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
