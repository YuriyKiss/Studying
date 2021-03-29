using System;
using System.Collections.Generic;
using Xunit;
using Microsoft.AspNetCore.Mvc;

using Flight_Web_API.Controllers;
using Flight_Web_API.Models;

namespace FlightTests
{
    public class GetAllTest
    {
        FlightsController controller;
        FlightControllerServiceMock service;

        public GetAllTest()
        {
            service = new FlightControllerServiceMock();
            controller = new FlightsController(service);
        }

        [Fact]
        public void GetAll_ReturnsOkResponse()
        {
            var result = controller.GetAll(null, null, null, 0, 0);

            Assert.IsType<OkObjectResult>(result);
        }

        [Fact]
        public void GetAll_ReturnsList()
        {
            var result = service.GetAll(null, null, null, 0, 0);

            Assert.IsType<List<Flight>>(result.result);
            Assert.Equal(5, result.count);
        }

        [Fact]
        public void GetAll_Search()
        {
            var result = service.GetAll("ukra", null, null, 0, 0);

            Assert.Equal(1, result.result[0].ID);
            Assert.Equal(1, result.count);
        }

        [Fact]
        public void GetAll_Sort()
        {
            var result = service.GetAll(null, "TicketPrice", null, 0, 0);

            Assert.Equal(3, result.result[0].ID);

            var result2 = service.GetAll(null, null, "desc", 0, 0);

            Assert.Equal(5, result2.result[0].ID);
        }

        [Fact]
        public void GetAll_Paginate()
        {
            var result = service.GetAll(null, null, null, 3, 2);
            Assert.Equal(1, result.count);
            result = service.GetAll(null, null, null, 0, 2);
            Assert.Equal(2, result.count);
            result = service.GetAll(null, null, null, 2, 0);
            Assert.Equal(0, result.count);
        }
    }

    public class GetOneTest
    {
        FlightsController controller;
        FlightControllerServiceMock service;

        public GetOneTest()
        {
            service = new FlightControllerServiceMock();
            controller = new FlightsController(service);
        }

        [Fact]
        public void GetOne_GoodID_ReturnsOK()
        {
            var result = controller.GetOne(1);

            Assert.IsType<OkObjectResult>(result);
        }

        [Fact]
        public void GetOne_GoodID_ReturnsCorrectFlight()
        {
            var result = (OkObjectResult)controller.GetOne(1);

            var data = Assert.IsType<Flight>(result.Value);
            Assert.Equal(1300, data.TicketPrice);
        }

        [Fact]
        public void GetOne_BadID_ReturnsNotFound()
        {
            var result = controller.GetOne(0);

            Assert.IsType<NotFoundObjectResult>(result);
        }

        [Fact]
        public void GetOne_BadID_ReturnsTextResponse()
        {
            var result = (NotFoundObjectResult)controller.GetOne(0);

            Assert.Equal("Flight with such ID was not found", result.Value);
        }
    }

    public class DeleteTest
    {
        FlightsController controller;
        FlightControllerServiceMock service;

        public DeleteTest()
        {
            service = new FlightControllerServiceMock();
            controller = new FlightsController(service);
        }

        [Fact]
        public void Delete_GoodID()
        {
            var result = controller.Delete(1);

            Assert.IsType<AcceptedResult>(result);

            Assert.IsType<NotFoundObjectResult>(controller.GetOne(1));
        }

        [Fact]
        public void Delete_BadID()
        {
            var result = controller.Delete(0);

            Assert.IsType<NotFoundObjectResult>(result);

            Assert.Equal("Flight with such ID was not found", ((NotFoundObjectResult)result).Value);
        }
    }

    public class CreateTest
    {
        FlightsController controller;
        FlightControllerServiceMock service;
        Flight toAdd;

        public CreateTest()
        {
            service = new FlightControllerServiceMock();
            controller = new FlightsController(service);

            toAdd = new Flight
            {
                ID = 6,
                DepartureCountry = "Italy",
                ArrivalCountry = "England",
                DepartureTime = new DateTime(2021, 07, 22, 15, 0, 0),
                ArrivalTime = new DateTime(2021, 07, 22, 16, 0, 0),
                TicketPrice = 2205,
                CompanyName = "Ryanair"
            };
        }

        [Fact]
        public void Create_GoodID()
        {
            var result = controller.Create(toAdd);

            Assert.IsType<CreatedResult>(result);

            Assert.Equal("api/flights/6", ((CreatedResult)result).Location);
            Assert.Equal("Flight was created successfully", ((CreatedResult)result).Value);

            Assert.Equal(toAdd, ((OkObjectResult)controller.GetOne(6)).Value);
        }

        [Fact]
        public void Create_TakenID()
        {
            toAdd.ID = 1;
            var result = controller.Create(toAdd);

            Assert.IsType<BadRequestObjectResult>(result);
            Assert.Equal("Flight ID already exist", ((BadRequestObjectResult)result).Value);
        }
    }

    public class EditTest
    {
        FlightsController controller;
        FlightControllerServiceMock service;

        public EditTest()
        {
            service = new FlightControllerServiceMock();
            controller = new FlightsController(service);
        }

        [Fact]
        public void Edit_BadID()
        {
            var result = controller.Edit(10, new Flight());

            Assert.IsType<NotFoundObjectResult>(result);

            Assert.Equal("Flight ID does not exist", ((NotFoundObjectResult)result).Value);
        }
    }
}